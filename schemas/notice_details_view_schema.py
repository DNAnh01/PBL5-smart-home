from typing import List, Dict
from pydantic import BaseModel

class NoticeDetailsView(BaseModel):
    notice_details_view_document_ID = "NoticeDetailsViewDocumentID"
    info_details: List[Dict[str, str]]
    class Config:
        schema_extra = {
            "example": {
                "info_details": [{"timestamp": "12:34:56", "description": "", "image_encoded_pred": ""},
                                {"timestamp": "12:40:00", "description": "", "image_encoded_pred": ""}]
            }
        }