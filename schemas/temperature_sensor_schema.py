from pydantic import BaseModel

class TemperatureSensor(BaseModel):
    temperature_sensor_document_ID = "TemperatureSensorDocumentID"
    timestamp: str
    data: int

    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2023-04-09 12:34:56",
                "data": 32.00
            }
        }