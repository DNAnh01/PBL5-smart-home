from daos.camera_dao import CameraDao
from services.gatehouse_service import GatehouseService
from schemas.camera_schema import Camera
from z_face_recognition.face_rec_encoded_img import FaceRecEncodedImg

camera_dao = CameraDao()

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
        for image_encoded in camera_update.images_encoded:
            pred = FaceRecEncodedImg(image_encoded)
            print(pred.face_rec_encoded_img()[0])

            



        # print("camera_update.images_encoded: ", camera_update.images_encoded)


        
        '''
        ['hello', 'image_encoded_2', 'image_encoded_3', 'image_encoded_4', 'image_encoded_5', 'image_encoded_6', 'image_encoded_7', 'image_encoded_8', 'image_encoded_9', 'image_encoded_10']
        '''
    
        '''
        camera_update:  timestamp='2023-04-09 12:34:56' description='description' images_encoded=['image_encoded_1', 'image_encoded_2', 'image_encoded_3', 'image_encoded_4', 'image_encoded_5', 'image_encoded_6', 'image_encoded_7', 'image_encoded_8', 'image_encoded_9', 'image_encoded_10'] camera_document_ID='CameraDocumentID' 
        '''
        return camera_dao.update(camera_document_ID, camera_update)
    
    
