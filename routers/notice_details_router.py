from fastapi import APIRouter, Body, HTTPException
from services.notice_details_service import NoticeDetailsService
from schemas.notice_details_schema import NoticeDetails

router = APIRouter()
notice_details_service = NoticeDetailsService()

@router.post("/notice_details/create", response_model=NoticeDetails, tags=["notice details"])
async def create_notice_details(notice_details_create: NoticeDetails = Body(...)) -> NoticeDetails:
    return notice_details_service.create_notice_details(notice_details_create)

@router.get("/notice_details/get/{notice_details_document_ID}", response_model=NoticeDetails, tags=["notice details"])
async def get_notice_details(notice_details_document_ID: str) -> NoticeDetails:
    result = notice_details_service.get_notice_details(notice_details_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="notice details not found.")
    return result

