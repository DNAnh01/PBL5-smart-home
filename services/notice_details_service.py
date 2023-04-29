from daos.notice_details_dao import NoticeDetailsDao
from schemas.notice_details_schema import NoticeDetails

notice_details_dao = NoticeDetailsDao()

class NoticeDetailsService:
    def create_notice_details(self, notice_details_create: NoticeDetails) -> NoticeDetails:
        return notice_details_dao.create(notice_details_create)

    def get_notice_details(self, notice_details_document_ID: str) -> NoticeDetails:
        return notice_details_dao.get(notice_details_document_ID)
    
    def update_notice_details(self, notice_details_document_ID: str, notice_details_update: NoticeDetails) -> NoticeDetails:
        return notice_details_dao.update(notice_details_document_ID, notice_details_update)
    
    
