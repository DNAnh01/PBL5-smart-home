from daos.notice_details_view_dao import NoticeDetailsViewDao
from schemas.notice_details_view_schema import NoticeDetailsView

notice_details_view_dao = NoticeDetailsViewDao()

class NoticeDetailsViewService:

    def create_notice_details_view(self, notice_details_view_create: NoticeDetailsView) -> NoticeDetailsView:
        return notice_details_view_dao.create(notice_details_view_create)

    def get_notice_details_view(self, notice_details_view_document_ID: str) -> NoticeDetailsView:
        return notice_details_view_dao.get(notice_details_view_document_ID)
   
    def update_notice_details_view(self, notice_details_view_document_ID: str, notice_details_view_update: NoticeDetailsView) -> NoticeDetailsView:
        return notice_details_view_dao.update(notice_details_view_document_ID, notice_details_view_update)