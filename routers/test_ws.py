from fastapi import APIRouter, WebSocket, Body
from fastapi.websockets import WebSocketDisconnect
import asyncio
from services.sensors_service import SensorsService 
from schemas.sensors_schema import Sensors

router = APIRouter()
connected_clients = set()
sensors_service = SensorsService()

@router.put("/ws", response_model=Sensors, tags=["test"])
async def websocket_endpoint(websocket: WebSocket, sensors_json: Sensors = Body(...)):
    await websocket.accept()
    connected_clients.add(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            # Xử lý dữ liệu nhận được từ nhà thông minh
            print("data", data)
            print("sensors_json", sensors_json)
            # sensors_service.update_sensors(sensors_document_ID, sensors_update)
            # Ví dụ: led_service.update_led(data)
            
            # Gửi dữ liệu cập nhật cho tất cả các client đang kết nối
            for client in connected_clients:
                await client.send_text(data)
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
