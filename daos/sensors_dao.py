from database.connection import db
from schemas.sensors_schema import Sensors

class SensorsDao:
    collection_name = "Sensors"

    def create(self, sensors_create: Sensors) -> Sensors:
        data = sensors_create.dict()
        data["sensors_document_ID"] = str(data["sensors_document_ID"])
        doc_ref = db.collection(self.collection_name).document(sensors_create.sensors_document_ID)
        doc_ref.set(data)
        return self.get(sensors_create.sensors_document_ID)

    def get(self, sensors_document_ID: str) -> Sensors:
        doc_ref = db.collection(self.collection_name).document(sensors_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return Sensors(**doc.to_dict())
        return

    def update(self, sensors_document_ID: str, sensors_update: Sensors) -> Sensors:
        data = sensors_update.dict()
        doc_ref = db.collection(self.collection_name).document(sensors_document_ID)
        doc_ref.update(data)
        return self.get(sensors_document_ID)