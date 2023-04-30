from pydantic import BaseModel
from typing import List, Optional

class NoticeDetails(BaseModel):
    notice_details_document_ID = "NoticeDetailsDocumentID"
    timestamp: str
    info: List[str]
    image_encoded_pred: List[str]

    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2023-04-09 12:34:56",
                "info": [   
                            "info_0",
                            "info_1",
                            "info_2",
                            "info_3",
                            "info_4"
                        ],

                "image_encoded_pred":[   
                                        "image_encoded_pred_0", 
                                        "image_encoded_pred_1",
                                        "image_encoded_pred_2",
                                        "image_encoded_pred_3",
                                        "image_encoded_pred_4"
                                    ]
            }
        }