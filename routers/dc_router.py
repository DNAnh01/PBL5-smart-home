from fastapi import APIRouter, Body, HTTPException
from services.dc_service import DCService
from schemas.dc_schema import DC

router = APIRouter()
dc_service = DCService()

@router.post("/dc/create", response_model=DC, tags=["dc"])
async def create_dc(dc_create: DC = Body(...)) -> DC:
    return dc_service.create_dc(dc_create)

@router.get("/dc/get/{dc_document_ID}", response_model=DC, tags=["dc"])
async def get_dc(dc_document_ID: str) -> DC:
    result = dc_service.get_dc(dc_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="dc not found.")
    return result

@router.put("/dc/update/{dc_document_ID}", response_model=DC, tags=["dc"])
async def update_dc(dc_document_ID: str, dc_update: DC = Body(...)) -> DC:
    result = dc_service.get_dc(dc_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="dc not found.")
    return dc_service.update_dc(dc_document_ID, dc_update)