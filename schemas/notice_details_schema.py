from typing import List, Optional
from pydantic import BaseModel


class NoticeDetails(BaseModel):
    notice_details_document_ID = "NoticeDetailsDocumentID"
    timestamp: str
    description: Optional[str] = None
    details_info: List[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2023-04-09 12:34:56",
                "description": "description",
                "details_info": [["info_1", "image_encoded_pred_1"], 
                                   ["info_2", "image_encoded_pred_2"],
                                   ["info_3", "image_encoded_pred_3"],
                                   ["info_4", "image_encoded_pred_4"],
                                   ["info_5", "image_encoded_pred_5"],
                                   ["info_6", "image_encoded_pred_6"],
                                   ["info_7", "image_encoded_pred_7"],
                                   ["info_8", "image_encoded_pred_8"],
                                   ["info_9", "image_encoded_pred_9"],
                                   ["info_10", "image_encoded_pred_10"]]
            }
        }