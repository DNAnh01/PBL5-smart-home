from fastapi import APIRouter, Body, HTTPException
from services.humidity_sensor_service import HumiditySensorService
from schemas.humidity_sensor_schema import HumiditySensor

router = APIRouter()
humidity_sensor_service = HumiditySensorService()


@router.post("/humidity_sensor/create", response_model=HumiditySensor, tags=["humidity sensor"])
async def create_humidity_sensor(humidity_sensor_create: HumiditySensor = Body(...)) -> HumiditySensor:
    return humidity_sensor_service.create_humidity_sensor(humidity_sensor_create)


@router.get("/humidity_sensor/get", response_model=HumiditySensor, tags=["humidity sensor"])
async def get_humidity_sensor() -> HumiditySensor:
    result = humidity_sensor_service.get_humidity_sensor()
    if not result:
        raise HTTPException(status_code=404, detail="humidity sensor not found.")
    return result

@router.put("temperature_sensor/update", response_model=HumiditySensor, tags=["humidity sensor"])
async def update_humidity_sensor(humidity_sensor_update: HumiditySensor = Body(...)) -> HumiditySensor:
    return humidity_sensor_service.update_humidity_sensor(humidity_sensor_update)

