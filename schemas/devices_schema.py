from pydantic import BaseModel

class Devices(BaseModel):
    devices_document_ID = "DevicesDocumentID"
    gatehouse_status: int
    led_status: int
    dc_status: int

    class Config:
        schema_extra = {
            "example": {
                "gatehouse_status": 0,
                "led_status": 0,
                "dc_status": 0
            }
        }