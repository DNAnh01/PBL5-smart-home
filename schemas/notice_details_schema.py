from pydantic import BaseModel

class NoticeDetails(BaseModel):
    notice_details_document_ID = "NoticeDetailsDocumentID"
    timestamp: str
    description: str
    image_encoded_pred: str

    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2023-04-09 12:34:56",
                "description": "description",
                "image_encoded_pred": "img_encode_pred"
            }
        }