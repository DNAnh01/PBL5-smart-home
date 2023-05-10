from fastapi import APIRouter, Body, HTTPException
from services.devices_service import DevicesService
from schemas.devices_schema import Devices

router = APIRouter()
devices_service = DevicesService()

@router.post("/devices/create", response_model=Devices, tags=["devices"])
async def create_devices(devices_create: Devices = Body(...)) -> Devices:
    return devices_service.create_devices(devices_create)

@router.get("/devices/get/{devices_document_ID}", response_model=Devices, tags=["devices"])
async def get_devices(devices_document_ID: str) -> Devices:
    result = devices_service.get_devices(devices_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="devices not found.")
    return result

@router.put("/devices/update/{devices_document_ID}", response_model=Devices, tags=["devices"])
async def update_devices(devices_document_ID: str, devices_update: Devices = Body(...)) -> Devices:
    result = devices_service.get_devices(devices_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="devices not found.")
    return devices_service.update_devices(devices_document_ID, devices_update)