# from typing import List

from daos.camera_dao import CameraDao
from schemas.camera_schema import Camera

camera_dao = CameraDao()

class CameraService:
    def create_camera(self, camera_create: Camera) -> Camera:
        return camera_dao.create(camera_create)

    def get_camera(self) -> Camera:
        return camera_dao.get()
    
    def update_camera(self, camera_update: Camera) -> Camera:
        return camera_dao.update(camera_update)
