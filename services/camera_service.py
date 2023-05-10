from daos.camera_dao import CameraDao
from schemas.camera_schema import Camera

from services.devices_service import DevicesService
from schemas.devices_schema import Devices

from services.notice_details_service import NoticeDetailsService
from schemas.notice_details_schema import NoticeDetails

from services.notice_details_view_service import NoticeDetailsViewService
from schemas.notice_details_view_schema import NoticeDetailsView
from collections import deque

from z_face_recognition.face_rec_encoded_img_MTCNN import face_rec_encoded_imgs

camera_dao = CameraDao()
devices_service = DevicesService()
notice_details_service = NoticeDetailsService()

notice_details_view_service = NoticeDetailsViewService()

class CameraService:
    def create_camera(self, camera_create: Camera) -> Camera:
        return camera_dao.create(camera_create)

    def get_camera(self, camera_document_ID: str) -> Camera:
        return camera_dao.get(camera_document_ID)
    
    def update_camera(self, camera_document_ID: str, camera_update: Camera) -> Camera:
        '''
            Khi sử dụng router update camera:
            1. pred encode imgs
            2. đưa ra quyết định mở cửa (cổng), update gatehouse
            3. update notice_details , notice_details_view để app android get về show  
        '''
        notice_details_view = notice_details_view_service.get_notice_details_view(
            notice_details_view_document_ID="NoticeDetailsViewDocumentID")
        notice_details_current = notice_details_service.get_notice_details(
            notice_details_document_ID="NoticeDetailsDocumentID")
        
        def handel_update_notice_details_view(notice_details_view, notice_details_current):
            notice_details = {
                                "description": notice_details_current.description,
                                "timestamp": notice_details_current.timestamp,
                                "image_encoded_pred": notice_details_current.image_encoded_pred
                            }
            notice_details_info_update = deque(notice_details_view.info_details, maxlen=5)
            notice_details_info_update.append(notice_details)
            notice_details_info_update = list(notice_details_info_update)
            notice_details_view_service.update_notice_details_view(notice_details_view_document_ID=
                                                                "NoticeDetailsViewDocumentID",
                                                                notice_details_view_update=NoticeDetailsView(info_details=notice_details_info_update))
        
        devices_current = devices_service.get_devices(devices_document_ID="DevicesDocumentID")
        
        
        def handel_update_devices_gatehouse(devices_current, status):
            devices_service.update_devices(devices_document_ID="DevicesDocumentID",
                                           devices_update=Devices(gatehouse_status=status,
                                                                  led_status=devices_current.led_status,
                                                                  dc_status=devices_current.dc_status))
        # 1. pred encode imgs
        pred_encode_imgs = face_rec_encoded_imgs(camera_update.images_encoded)
        '''
            [['NguyenAnh: 79.03%', 'image_encoded_pred_0'],
            ['NguyenAnh: 79.03%', 'image_encoded_pred_1'],
            ['NguyenAnh: 79.03%', 'image_encoded_pred_3']]

        '''
        #  2. đưa ra quyết định mở cửa (cổng), update gatehouse
        recognized_people = {}
        for person in pred_encode_imgs:
            name = person[0].split(':')[0]
            confidence = float(person[0].split(':')[1].strip('%'))
            if name in ['NguyenAnh', 'NgocAnh', 'HongVan', 'NhuQuynh']:
                recognized_people[name] = confidence
        if recognized_people:
            max_confidence = max(recognized_people.values())
            if max_confidence > 75:
                person_to_open = [k for k, v in recognized_people.items() if v == max_confidence][0]
                # update gatehouse
                # devices_service.update_devices("DevicesDocumentID",
                #  
                #                                   Devices(gatehouse_status=1))

                handel_update_devices_gatehouse(devices_current=devices_current, status=1)
                # update notice details
                notice_details_service.update_notice_details("NoticeDetailsDocumentID",
                                                             NoticeDetails(
                                                                timestamp=camera_update.timestamp,
                                                                description=str(f"{person_to_open} - {max_confidence} %"),
                                                                image_encoded_pred=pred_encode_imgs[0][1]))
                # update notice details view
                handel_update_notice_details_view(notice_details_view, notice_details_current)
                print(f"Opening gate for {person_to_open}")
            else:
                # update gatehouse
                # devices_service.update_devices("DevicesDocumentID",Devices(gatehouse_status=0))
                handel_update_devices_gatehouse(devices_current=devices_current, status=0)
                # update notice details view
                handel_update_notice_details_view(notice_details_view, notice_details_current)
                print("Not enough confidence to open the gate")
        else:
            # devices_service.update_devices("DevicesDocumentID",Devices(gatehouse_status=0))
            handel_update_devices_gatehouse(devices_current=devices_current, status=0)
            # update notice details view
            handel_update_notice_details_view(notice_details_view, notice_details_current)
            print("Unknown person detected")
        #  3. update notice_details để app android get về show 
        return camera_dao.update(camera_document_ID, camera_update)
    
    
