from database.connection import db
from schemas.notice_details_view_schema import NoticeDetailsView

class NoticeDetailsViewDao:
    collection_name = "NoticeDetailsView"

    def create(self, notice_details_view_create: NoticeDetailsView) -> NoticeDetailsView:
        data = notice_details_view_create.dict()
        data["notice_details_view_document_ID"] = str(data["notice_details_view_document_ID"])
        doc_ref = db.collection(self.collection_name).document(notice_details_view_create.notice_details_view_document_ID)
        doc_ref.set(data)
        return self.get(notice_details_view_create.notice_details_view_document_ID)

    def get(self, notice_details_view_document_ID: str) -> NoticeDetailsView:
        doc_ref = db.collection(self.collection_name).document(notice_details_view_document_ID)
        doc = doc_ref.get()
        if doc != None:
            return NoticeDetailsView(**doc.to_dict())
        return

    def update(self, notice_details_view_document_ID: str, notice_details_view_update: NoticeDetailsView) -> NoticeDetailsView:
        data = notice_details_view_update.dict()
        doc_ref = db.collection(self.collection_name).document(notice_details_view_document_ID)
        doc_ref.update(data)
        return self.get(notice_details_view_document_ID)