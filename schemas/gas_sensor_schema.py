from pydantic import BaseModel

class GasSensor(BaseModel):
    gas_sensor_document_ID = "GasSensorDocumentID"
    timestamp: str
    data: int

    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2023-04-09 12:34:56",
                "data": 1
            }
        }