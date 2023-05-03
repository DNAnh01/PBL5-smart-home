from typing import List, Dict, Union
from pydantic import BaseModel

class SensorsView(BaseModel):
    sensors_view_document_ID = "SensorsViewDocumentID"
    temperature_sensor: List[Dict[str, Union[str, int]]]
    humidity_sensor: List[Dict[str, Union[str, int]]]
    gas_sensor: List[Dict[str, Union[str, int]]]
    class Config:
        schema_extra = {
            "example": {
                "temperature_sensor": [{"timestamp": "12:34:56", "data": 32},
                                        {"timestamp": "12:34:58", "data": 32},
                                        {"timestamp": "12:35:00", "data": 32},
                                        {"timestamp": "12:35:02", "data": 33},
                                        {"timestamp": "12:35:04", "data": 32},
                                        {"timestamp": "12:35:06", "data": 34},
                                        {"timestamp": "12:35:08", "data": 32},
                                        {"timestamp": "12:35:10", "data": 33},
                                        {"timestamp": "12:35:12", "data": 32},
                                        {"timestamp": "12:35:14", "data": 34}],
                
                "humidity_sensor": [{"timestamp": "12:34:56", "data": 71},
                                    {"timestamp": "12:34:58", "data": 71},
                                    {"timestamp": "12:35:00", "data": 72},
                                    {"timestamp": "12:35:02", "data": 71},
                                    {"timestamp": "12:35:04", "data": 71},
                                    {"timestamp": "12:35:06", "data": 71},
                                    {"timestamp": "12:35:08", "data": 73},
                                    {"timestamp": "12:35:10", "data": 71},
                                    {"timestamp": "12:35:12", "data": 70},
                                    {"timestamp": "12:35:14", "data": 71}],
                
                "gas_sensor": [{"timestamp": "12:34:56", "data": 0},
                                {"timestamp": "12:34:58", "data": 0},
                                {"timestamp": "12:35:00", "data": 1},
                                {"timestamp": "12:35:02", "data": 1},
                                {"timestamp": "12:35:04", "data": 0},
                                {"timestamp": "12:35:06", "data": 0},
                                {"timestamp": "12:35:08", "data": 0},
                                {"timestamp": "12:35:10", "data": 0},
                                {"timestamp": "12:35:12", "data": 0},
                                {"timestamp": "12:35:14", "data": 0}]
            }
        }