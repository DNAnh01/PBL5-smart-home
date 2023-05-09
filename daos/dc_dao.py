from database.connection import db
from schemas.dc_schema import DC

class DCDao:
    collection_name = "DC"

    def create(self, dc_create: DC) -> DC:
        data = dc_create.dict()
        data["dc_document_ID"] = str(data["dc_document_ID"])
        doc_ref = db.collection(self.collection_name).document(dc_create.dc_document_ID)
        doc_ref.set(data)
        return self.get(dc_create.dc_document_ID)

    def get(self, dc_document_ID: str) -> DC:
        doc_ref = db.collection(self.collection_name).document(dc_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return DC(**doc.to_dict())
        return

    def update(self, dc_document_ID: str, dc_update: DC) -> DC:
        data = dc_update.dict()
        doc_ref = db.collection(self.collection_name).document(dc_document_ID)
        doc_ref.update(data)
        return self.get(dc_document_ID)
