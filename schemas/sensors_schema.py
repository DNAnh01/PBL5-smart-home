from pydantic import BaseModel

class Sensors(BaseModel):
    sensors_document_ID = "SensorsDocumentID"
    timestamp: str
    temperature_sensor_data: int
    humidity_sensor_data: int
    gas_sensor_data: int

    class Config:
        schema_extra = {
            "example": {
                "timestamp": "12:34:56",
                "temperature_sensor_data": 32,
                "humidity_sensor_data": 71,
                "gas_sensor_data": 0
            }
        }