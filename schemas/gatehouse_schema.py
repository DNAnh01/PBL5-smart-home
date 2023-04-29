from pydantic import BaseModel

class GateHouse(BaseModel):
    gatehouse_document_ID = "GatehouseDocumentID"
    timestamp: str
    status: bool
    
    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2023-04-09 12:34:56",
                "status": False 
            }
        }