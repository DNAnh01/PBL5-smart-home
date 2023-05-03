from fastapi import APIRouter, Body, HTTPException
from services.notice_details_view_service import NoticeDetailsViewService 
from schemas.notice_details_view_schema import NoticeDetailsView

router = APIRouter()
notice_details_view_service = NoticeDetailsViewService()


@router.post("/notice_details_view/create", response_model=NoticeDetailsView, tags=["notice details view"])
async def create_notice_details_view(notice_details_view_create: NoticeDetailsView = Body(...)) -> NoticeDetailsView:
    return notice_details_view_service.create_notice_details_view(notice_details_view_create)


@router.get("/notice_details_view/get/{notice_details_view_document_ID}", response_model=NoticeDetailsView, tags=["notice details view"])
async def get_notice_details_view(notice_details_view_document_ID: str) -> NoticeDetailsView:
    result = notice_details_view_service.get_notice_details_view(notice_details_view_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="notice details view not found.")
    return result