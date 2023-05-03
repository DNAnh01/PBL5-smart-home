from fastapi import APIRouter, Body, HTTPException
from services.led_service import LedService
from schemas.led_schema import Led

router = APIRouter()
led_service = LedService()

@router.post("/led/create", response_model=Led, tags=["led"])
async def create_led(led_create: Led = Body(...)) -> Led:
    return led_service.create_led(led_create)

@router.get("/led/get/{led_document_ID}", response_model=Led, tags=["led"])
async def get_led(led_document_ID: str) -> Led:
    result = led_service.get_led(led_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="led not found.")
    return result

@router.put("/led/update/{led_document_ID}", response_model=Led, tags=["led"])
async def update_led(led_document_ID: str, led_update: Led = Body(...)) -> Led:
    result = led_service.get_led(led_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="led not found.")
    return led_service.update_led(led_document_ID, led_update)