from database.connection import db
from schemas.temperature_sensor_schema import TemperatureSensor

class TemperatureSensorDao:
    collection_name = "TemperatureSensor"

    def create(self, temperature_sensor_create: TemperatureSensor) -> TemperatureSensor:
        data = temperature_sensor_create.dict()
        data["temperature_sensor_document_ID"] = str(data["temperature_sensor_document_ID"])
        doc_ref = db.collection(self.collection_name).document(temperature_sensor_create.temperature_sensor_document_ID)
        doc_ref.set(data)
        return self.get(temperature_sensor_create.temperature_sensor_document_ID)

    def get(self, temperature_sensor_document_ID: str) -> TemperatureSensor:
        doc_ref = db.collection(self.collection_name).document(temperature_sensor_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return TemperatureSensor(**doc.to_dict())
        return


    def update(self, temperature_sensor_document_ID: str, temperature_sensor_update: TemperatureSensor) -> TemperatureSensor:
        data = temperature_sensor_update.dict()
        doc_ref = db.collection(self.collection_name).document(temperature_sensor_document_ID)
        doc_ref.update(data)
        return self.get(temperature_sensor_document_ID)