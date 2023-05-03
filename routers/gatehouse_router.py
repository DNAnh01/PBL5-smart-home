from fastapi import APIRouter, Body, HTTPException
from services.gatehouse_service import GatehouseService
from schemas.gatehouse_schema import GateHouse

router = APIRouter()
gatehouse_service = GatehouseService()

@router.post("/gatehouse/create", response_model=GateHouse, tags=["gatehouse"])
async def create_gatehouse(gatehouse_create: GateHouse = Body(...)) -> GateHouse:
    return gatehouse_service.create_gatehouse(gatehouse_create)

@router.get("/gatehouse/get/{gatehouse_document_ID}", response_model=GateHouse, tags=["gatehouse"])
async def get_gatehouse(gatehouse_document_ID: str) -> GateHouse:
    result = gatehouse_service.get_gatehouse(gatehouse_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="gatehouse not found.")
    return result

@router.put("/gatehouse/update/{gatehouse_document_ID}", response_model=GateHouse, tags=["gatehouse"])
async def update_gatehouse(gatehouse_document_ID: str, gatehouse_update: GateHouse = Body(...)) -> GateHouse:
    result = gatehouse_service.get_gatehouse(gatehouse_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="gatehouse not found.")
    return gatehouse_service.update_gatehouse(gatehouse_document_ID, gatehouse_update)