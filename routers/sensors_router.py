from fastapi import APIRouter, Body, HTTPException
from services.sensors_service import SensorsService 
from schemas.sensors_schema import Sensors

router = APIRouter()
sensors_service = SensorsService()


@router.post("/sensors/create", response_model=Sensors, tags=["sensors"])
async def create_sensors(sensors_create: Sensors = Body(...)) -> Sensors:
    return sensors_service.create_sensors(sensors_create)


@router.get("/sensors/get/{sensors_document_ID}", response_model=Sensors, tags=["sensors"])
async def get_sensors(sensors_document_ID: str) -> Sensors:
    result = sensors_service.get_sensors(sensors_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="sensors not found.")
    return result

@router.put("/sensors/update/{sensors_document_ID}", response_model=Sensors, tags=["sensors"])
async def update_sensors(sensors_document_ID: str, sensors_update: Sensors = Body(...)) -> Sensors:
    result = sensors_service.get_sensors(sensors_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="sensors not found.")
    return sensors_service.update_sensors(sensors_document_ID, sensors_update)

