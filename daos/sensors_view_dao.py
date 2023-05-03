from database.connection import db
from schemas.sensors_view_schema import SensorsView

class SensorsViewDao:
    collection_name = "SensorsView"

    def create(self, sensors_view_create: SensorsView) -> SensorsView:
        data = sensors_view_create.dict()
        data["sensors_view_document_ID"] = str(data["sensors_view_document_ID"])
        doc_ref = db.collection(self.collection_name).document(sensors_view_create.sensors_view_document_ID)
        doc_ref.set(data)
        return self.get(sensors_view_create.sensors_view_document_ID)

    def get(self, sensors_view_document_ID: str) -> SensorsView:
        doc_ref = db.collection(self.collection_name).document(sensors_view_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return SensorsView(**doc.to_dict())
        return

    def update(self, sensors_view_document_ID: str, sensors_view_update: SensorsView) -> SensorsView:
        data = sensors_view_update.dict()
        doc_ref = db.collection(self.collection_name).document(sensors_view_document_ID)
        doc_ref.update(data)
        return self.get(sensors_view_document_ID)