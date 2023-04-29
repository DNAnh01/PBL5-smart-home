from database.connection import db
from schemas.gas_sensor_schema import GasSensor

class GasSensorDao:
    collection_name = "GasSensor"

    def create(self, gas_sensor_create: GasSensor) -> GasSensor:
        data = gas_sensor_create.dict()
        data["gas_sensor_document_ID"] = str(data["gas_sensor_document_ID"])
        doc_ref = db.collection(self.collection_name).document(gas_sensor_create.gas_sensor_document_ID)
        doc_ref.set(data)
        return self.get(gas_sensor_create.gas_sensor_document_ID)

    def get(self, gas_sensor_document_ID: str) -> GasSensor:
        doc_ref = db.collection(self.collection_name).document(gas_sensor_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return GasSensor(**doc.to_dict())
        return


    def update(self, gas_sensor_document_ID: str, gas_sensor_update: GasSensor) -> GasSensor:
        data = gas_sensor_update.dict()
        doc_ref = db.collection(self.collection_name).document(gas_sensor_document_ID)
        doc_ref.update(data)
        return self.get(gas_sensor_document_ID)