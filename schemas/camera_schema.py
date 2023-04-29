from typing import List, Optional
from pydantic import BaseModel


class Camera(BaseModel):
    camera_document_ID = "CameraDocumentID"
    timestamp: str
    description: Optional[str] = None
    images_encoded: List[str]

    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2023-04-09 12:34:56",
                "description": "description",
                "images_encoded": ["image_encoded_1", 
                                   "image_encoded_2",
                                   "image_encoded_3",
                                   "image_encoded_4",
                                   "image_encoded_5",
                                   "image_encoded_6",
                                   "image_encoded_7",
                                   "image_encoded_8",
                                   "image_encoded_9",
                                   "image_encoded_10"]
            }
        }