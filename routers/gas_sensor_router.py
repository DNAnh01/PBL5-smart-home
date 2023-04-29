from fastapi import APIRouter, Body, HTTPException
from services.gas_sensor_service import GasSensorService
from schemas.gas_sensor_schema import GasSensor

router = APIRouter()
gas_sensor_service = GasSensorService()


@router.post("/gas_sensor/create", response_model=GasSensor, tags=["gas sensor"])
async def create_gas_sensor(gas_sensor_create: GasSensor = Body(...)) -> GasSensor:
    return gas_sensor_service.create_gas_sensor(gas_sensor_create)


@router.get("/gas_sensor/get/{gas_sensor_document_ID}", response_model=GasSensor, tags=["gas sensor"])
async def get_gas_sensor(gas_sensor_document_ID: str) -> GasSensor:
    result = gas_sensor_service.get_gas_sensor(gas_sensor_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="gas sensor not found.")
    return result

@router.put("/gas_sensor/update/{gas_sensor_document_ID}", response_model=GasSensor, tags=["gas sensor"])
async def update_gas_sensor(gas_sensor_document_ID: str, gas_sensor_update: GasSensor = Body(...)) -> GasSensor:
    result = gas_sensor_service.get_gas_sensor(gas_sensor_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="gas sensor not found.")
    return gas_sensor_service.update_gas_sensor(gas_sensor_document_ID, gas_sensor_update)

