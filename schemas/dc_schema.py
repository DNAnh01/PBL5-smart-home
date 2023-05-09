from pydantic import BaseModel

class DC(BaseModel):
    dc_document_ID = "DCDocumentID"
    status: int
    
    class Config:
        schema_extra = {
            "example": {
                "status": 0 
            }
        }