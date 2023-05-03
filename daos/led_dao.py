from database.connection import db
from schemas.led_schema import Led

class LedDao:
    collection_name = "Led"

    def create(self, led_create: Led) -> Led:
        data = led_create.dict()
        data["led_document_ID"] = str(data["led_document_ID"])
        doc_ref = db.collection(self.collection_name).document(led_create.led_document_ID)
        doc_ref.set(data)
        return self.get(led_create.led_document_ID)

    def get(self, led_document_ID: str) -> Led:
        doc_ref = db.collection(self.collection_name).document(led_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return Led(**doc.to_dict())
        return

    def update(self, led_document_ID: str, led_update: Led) -> Led:
        data = led_update.dict()
        doc_ref = db.collection(self.collection_name).document(led_document_ID)
        doc_ref.update(data)
        return self.get(led_document_ID)
