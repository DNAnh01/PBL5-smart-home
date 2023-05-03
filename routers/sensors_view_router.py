from fastapi import APIRouter, Body, HTTPException
from services.sensors_view_service import SensorsViewService 
from schemas.sensors_view_schema import SensorsView

router = APIRouter()
sensors_view_service = SensorsViewService()


@router.post("/sensors_view/create", response_model=SensorsView, tags=["sensors view"])
async def create_sensors_view(sensors_view_create: SensorsView = Body(...)) -> SensorsView:
    return sensors_view_service.create_sensors_view(sensors_view_create)


@router.get("/sensors_view/get/{sensors_view_document_ID}", response_model=SensorsView, tags=["sensors view"])
async def get_sensors_view(sensors_view_document_ID: str) -> SensorsView:
    result = sensors_view_service.get_sensors_view(sensors_view_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="sensors view not found.")
    return result