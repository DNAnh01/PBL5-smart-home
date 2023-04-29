from pydantic import BaseModel

class HumiditySensor(BaseModel):
    humidity_sensor_document_ID = "HumiditySensorDocumentID"
    timestamp: str
    data: int
    
    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2023-04-09 12:34:56",
                "data": 20.00
            }
        }