from database.connection import db
from schemas.camera_schema import Camera
# from typing import List


class CameraDao:
    collection_name = "Camera"
    # camera_document_ID = "CameraDocumentID"
    def create(self, camera_create: Camera) -> Camera:
        data = camera_create.dict()
        data["camera_document_ID"] = str(data["camera_document_ID"])
        doc_ref = db.collection(self.collection_name).document(camera_create.camera_document_ID)
        doc_ref.set(data)
        return self.get(camera_create.camera_document_ID)

    def get(self, camera_document_ID: str) -> Camera:
        doc_ref = db.collection(self.collection_name).document(camera_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return Camera(**doc.to_dict())
        return


    def update(self, camera_document_ID: str, camera_update: Camera) -> Camera:
        data = camera_update.dict()
        doc_ref = db.collection(self.collection_name).document(camera_document_ID)
        doc_ref.update(data)
        return self.get(camera_document_ID)
