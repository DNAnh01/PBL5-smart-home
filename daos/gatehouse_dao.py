from database.connection import db
from schemas.gatehouse_schema import GateHouse

class GateHouseDao:
    collection_name = "Gatehouse"
    
    def create(self, gatehouse_create: GateHouse) -> GateHouse:
        data = gatehouse_create.dict()
        data["gatehouse_document_ID"] = str(data["gatehouse_document_ID"])
        doc_ref = db.collection(self.collection_name).document(gatehouse_create.gatehouse_document_ID)
        doc_ref.set(data)
        return self.get(gatehouse_create.gatehouse_document_ID)

    def get(self, gatehouse_document_ID: str) -> GateHouse:
        doc_ref = db.collection(self.collection_name).document(gatehouse_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return GateHouse(**doc.to_dict())
        return


    def update(self, gatehouse_document_ID: str, gatehouse_update: GateHouse) -> GateHouse:
        data = gatehouse_update.dict()
        doc_ref = db.collection(self.collection_name).document(gatehouse_document_ID)
        doc_ref.update(data)
        return self.get(gatehouse_document_ID)