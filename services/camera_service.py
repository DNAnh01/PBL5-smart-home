from daos.camera_dao import CameraDao
from services.gatehouse_service import GatehouseService
from schemas.camera_schema import Camera
from z_face_recognition.face_rec_encoded_img import face_rec_encoded_imgs

camera_dao = CameraDao()
gatehouse_service = GatehouseService()
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
                
                print(f"Opening gate for {person_to_open}")
                # logic để mở cửa ở đây
            else:
                print("Not enough confidence to open the gate")
        else:
            print("Unknown person detected")


        #  3. update notice_details để app android get về show 
        return camera_dao.update(camera_document_ID, camera_update)
    
    
