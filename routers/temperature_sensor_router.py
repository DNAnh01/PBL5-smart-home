from fastapi import APIRouter, Body, HTTPException
from services.temperature_sensor_service import TemperatureSensorService
from schemas.temperature_sensor_schema import TemperatureSensor

router = APIRouter()
temperature_sensor_service = TemperatureSensorService()


@router.post("/temperature_sensor/create", response_model=TemperatureSensor, tags=["temperature sensor"])
async def create_temperature_sensor(temperature_sensor_create: TemperatureSensor = Body(...)) -> TemperatureSensor:
    return temperature_sensor_service.create_temperature_sensor(temperature_sensor_create)


@router.get("/temperature_sensor/get", response_model=TemperatureSensor, tags=["temperature sensor"])
async def get_temperature_sensor() -> TemperatureSensor:
    result = temperature_sensor_service.get_temperature_sensor()
    if not result:
        raise HTTPException(status_code=404, detail="temperature sensor not found.")
    return result

@router.put("temperature_sensor/update", response_model=TemperatureSensor, tags=["temperature sensor"])
async def update_temperature_sensor(temperature_sensor_update: TemperatureSensor = Body(...)) -> TemperatureSensor:
    return temperature_sensor_service.update_temperature_sensor(temperature_sensor_update)

