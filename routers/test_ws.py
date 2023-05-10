from fastapi import APIRouter, WebSocket, Body
from fastapi.websockets import WebSocketDisconnect
import asyncio
from services.sensors_service import SensorsService 
from schemas.sensors_schema import Sensors
router = APIRouter()
connected_clients = {}  # Sử dụng dict để lưu trữ các client kết nối

sensors_service = SensorsService()

@router.put("/ws/test2", response_model=Sensors, tags=["test"])
async def websocket_endpoint(websocket: WebSocket, sensors_json: Sensors = Body(...)):
    await websocket.accept()
    connected_clients[websocket.client.host] = websocket  # Lưu trữ client theo địa chỉ IP
    try:
        while True:
            data = await websocket.receive_text()
            # Xử lý dữ liệu nhận được từ nhà thông minh
            print("data", data)
            # sensors_service.update_sensors(sensors_document_ID, sensors_update)
            
            # Gửi dữ liệu cập nhật cho client có địa chỉ IP cụ thể
            target_ip = "http://127.0.0.1:5000/"  # Địa chỉ IP cần gửi dữ liệu
            if target_ip in connected_clients:
                target_client = connected_clients[target_ip]
                await target_client.send_text(data)
    except WebSocketDisconnect:
        del connected_clients[websocket.client.host]  # Xóa client khỏi danh sách khi ngắt kết nối