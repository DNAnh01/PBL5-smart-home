from database.connection import db
from schemas.humidity_sensor_schema import HumiditySensor

class HumiditySensorDao:
    collection_name = "HumiditySensor"

    def create(self, humidity_sensor_create: HumiditySensor) -> HumiditySensor:
        data = humidity_sensor_create.dict()
        data["humidity_sensor_document_ID"] = str(data["humidity_sensor_document_ID"])
        doc_ref = db.collection(self.collection_name).document(humidity_sensor_create.humidity_sensor_document_ID)
        doc_ref.set(data)
        return self.get(humidity_sensor_create.humidity_sensor_document_ID)


    def get(self, humidity_sensor_document_ID: str) -> HumiditySensor:
        doc_ref = db.collection(self.collection_name).document(humidity_sensor_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return HumiditySensor(**doc.to_dict())
        return


    def update(self, humidity_sensor_document_ID: str, humidity_sensor_update: HumiditySensor) -> HumiditySensor:
        data = humidity_sensor_update.dict()
        doc_ref = db.collection(self.collection_name).document(humidity_sensor_document_ID)
        doc_ref.update(data)
        return self.get(humidity_sensor_document_ID)