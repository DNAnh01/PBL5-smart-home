from database.connection import db
from schemas.devices_schema import Devices

class DevicesDao:
    collection_name = "Devices"

    def create(self, devices_create: Devices) -> Devices:
        data = devices_create.dict()
        data["devices_document_ID"] = str(data["devices_document_ID"])
        doc_ref = db.collection(self.collection_name).document(devices_create.devices_document_ID)
        doc_ref.set(data)
        return self.get(devices_create.devices_document_ID)

    def get(self, devices_document_ID: str) -> Devices:
        doc_ref = db.collection(self.collection_name).document(devices_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return Devices(**doc.to_dict())
        return

    def update(self, devices_document_ID: str, devices_update: Devices) -> Devices:
        data = devices_update.dict()
        doc_ref = db.collection(self.collection_name).document(devices_document_ID)
        doc_ref.update(data)
        return self.get(devices_document_ID)
