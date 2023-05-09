from pydantic import BaseModel

class DC(BaseModel):
    dc_document_ID = "DCDocumentID"
    timestamp: str
    status: int
    
    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2023-04-09 12:34:56",
                "status": 0 
            }
        }