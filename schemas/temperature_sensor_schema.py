from pydantic import BaseModel, Field
from datetime import datetime, time

class TemperatureSensor(BaseModel):
    temperature_sensor_document_ID = "TemperatureSensorDocumentID"
    timestamp: datetime = Field(..., description="Timestamp of the image capture in ISO 8601 format")
    data: int
    
    @property
    def capture_time(self) -> time:
        return self.timestamp.time()
    
    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2023-04-09T12:34:56.789Z",
                "data": 32
            }
        }