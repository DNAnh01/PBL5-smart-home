from daos.camera_dao import CameraDao
from schemas.camera_schema import Camera

from services.gatehouse_service import GatehouseService
from schemas.gatehouse_schema import GateHouse

from services.notice_details_service import NoticeDetailsService
from schemas.notice_details_schema import NoticeDetails

from z_face_recognition.face_rec_encoded_img import face_rec_encoded_imgs

camera_dao = CameraDao()
gatehouse_service = GatehouseService()
notice_details_service = NoticeDetailsService()
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
            3. update notice_details để app android get về show  
        '''
        # 1. pred encode imgs
        pred_encode_imgs = face_rec_encoded_imgs(camera_update.images_encoded)
        '''
            [['NguyenAnh: 79.03%', 'image_encoded_pred_0'],
            ['NguyenAnh: 79.03%', 'image_encoded_pred_1'],
            ['NguyenAnh: 79.03%', 'image_encoded_pred_3'],
            ['NguyenAnh: 79.03%', 'image_encoded_pred_4'],
            ['NguyenAnh: 79.03%', 'image_encoded_pred_5']]
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
                gatehouse_service.update_gatehouse("GatehouseDocumentID",
                                                   GateHouse(
                                                                status=1,
                                                                timestamp=camera_update.timestamp))
                # update notice details
                notice_details_service.update_notice_details("NoticeDetailsDocumentID",
                                                             NoticeDetails(
                                                                timestamp=camera_update.timestamp,
                                                                info=[str(f"{person_to_open} - {max_confidence} %")],
                                                                image_encoded_pred=[pred_encode_imgs[0][1]]))
                print(f"Opening gate for {person_to_open}")
            else:
                # update gatehouse
                gatehouse_service.update_gatehouse("GatehouseDocumentID",GateHouse(status=0,timestamp=camera_update.timestamp))
                print("Not enough confidence to open the gate")
        else:
            gatehouse_service.update_gatehouse("GatehouseDocumentID",GateHouse(status=0,timestamp=camera_update.timestamp))
            print("Unknown person detected")


        #  3. update notice_details để app android get về show 
        return camera_dao.update(camera_document_ID, camera_update)
    
    
