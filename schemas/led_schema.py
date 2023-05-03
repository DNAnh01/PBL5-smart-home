from pydantic import BaseModel

class Led(BaseModel):
    led_document_ID = "LedDocumentID"
    status: int
    
    class Config:
        schema_extra = {
            "example": {
                "status": 0 
            }
        }