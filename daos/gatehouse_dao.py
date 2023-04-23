from database.connection import db
from schemas.gatehouse_schema import GateHouse

class GateHouseDao:
    collection_name = "gatehouse"
    gatehouse_document_ID = "GatehouseDocumentID"

    def create(self, gatehouse_create: GateHouse) -> GateHouse:
        data = gatehouse_create.dict()
        doc_ref = db.collection(self.collection_name).document(
            self.gatehouse_document_ID)
        doc_ref.set(data)
        return self.get()

    def get(self) -> GateHouse:
        doc_ref = db.collection(self.collection_name).document(
            self.gatehouse_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return GateHouse(**doc.to_dict())
        return


    def update(self, gatehouse_update: GateHouse) -> GateHouse:
        data = gatehouse_update.dict()
        doc_ref = db.collection(self.collection_name).document(
            self.gatehouse_document_ID)
        doc_ref.update(data)
        return self.get()