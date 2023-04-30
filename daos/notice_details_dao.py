from database.connection import db
from schemas.notice_details_schema import NoticeDetails

class NoticeDetailsDao:

    collection_name = "NoticeDetails"

    def create(self, notice_details_create: NoticeDetails) -> NoticeDetails:
        data = notice_details_create.dict()
        print(data)
        data["notice_details_document_ID"] = str(data["notice_details_document_ID"])
        doc_ref = db.collection(self.collection_name).document(notice_details_create.notice_details_document_ID)
        doc_ref.set(data)
        return self.get(notice_details_create.notice_details_document_ID)

    def get(self, notice_details_document_ID: str) -> NoticeDetails:
        doc_ref = db.collection(self.collection_name).document(notice_details_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return NoticeDetails(**doc.to_dict())
        return

    def update(self, notice_details_document_ID: str, notice_details_update: NoticeDetails) -> NoticeDetails:
        data = notice_details_update.dict()
        doc_ref = db.collection(self.collection_name).document(notice_details_document_ID)
        doc_ref.update(data)
        return self.get(notice_details_document_ID)