from pydantic import BaseModel, Field
from datetime import datetime

class GateHouse(BaseModel):
    gatehouse_document_ID = "GatehouseDocumentID"
    timestamp: datetime = Field(..., description="Timestamp of the image capture in ISO 8601 format")
    status: bool
    
    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2023-04-09T12:34:56.789Z",
                "status": False 
            }
        }