from fastapi import APIRouter, Body, HTTPException, WebSocket
from services.gatehouse_service import GatehouseService
from schemas.gatehouse_schema import GateHouse
import httpx


router = APIRouter()
gatehouse_service = GatehouseService()

@router.post("/gatehouse/create", response_model=GateHouse, tags=["gatehouse"])
async def create_gatehouse(gatehouse_create: GateHouse = Body(...)) -> GateHouse:
    return gatehouse_service.create_gatehouse(gatehouse_create)

@router.get("/gatehouse/get/{gatehouse_document_ID}", response_model=GateHouse, tags=["gatehouse"])
async def get_gatehouse(gatehouse_document_ID: str) -> GateHouse:
    result = gatehouse_service.get_gatehouse(gatehouse_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="gatehouse not found.")
    return result

# @router.put("/gatehouse/update/{gatehouse_document_ID}", response_model=GateHouse, tags=["gatehouse"])
# async def update_gatehouse(websocket: WebSocket, gatehouse_document_ID: str, gatehouse_update: GateHouse = Body(...)) -> GateHouse:
#     result = gatehouse_service.get_gatehouse(gatehouse_document_ID)
#     if not result:
#         raise HTTPException(status_code=404, detail="gatehouse not found.")
#     return gatehouse_service.update_gatehouse(gatehouse_document_ID, gatehouse_update)


@router.put("/gatehouse/home_sent/update/{gatehouse_document_ID}", response_model=GateHouse, tags=["gatehouse"])
async def update_gatehouse(gatehouse_document_ID: str, gatehouse_update: GateHouse = Body(...)) -> GateHouse:
    result = gatehouse_service.get_gatehouse(gatehouse_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="gatehouse not found.")
    
    # Gửi dữ liệu cập nhật cho app Android có địa chỉ IP cụ thể
    target_ip = "27.69.146.73"  # Địa chỉ IP cần gửi dữ liệu
    await send_json_to_android_app(target_ip, gatehouse_update)
    
    return gatehouse_service.update_gatehouse(gatehouse_document_ID, gatehouse_update)

async def send_json_to_android_app(ip: str, json_data: dict):
    url = f"http://{ip}/endpoint"  # Đường dẫn endpoint của app Android
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=json_data)
            
            if response.status_code == 200:
                print("Dữ liệu đã được gửi thành công tới app Android.")
            else:
                raise HTTPException(status_code=response.status_code, detail="Gửi dữ liệu tới app Android không thành công.")
    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=f"Lỗi khi gửi dữ liệu tới app Android: {exc}")

@router.put("/gatehouse/app_sent/update/{gatehouse_document_ID}", response_model=GateHouse, tags=["gatehouse"])
async def update_gatehouse(gatehouse_document_ID: str, gatehouse_update: GateHouse = Body(...)) -> GateHouse:
    result = gatehouse_service.get_gatehouse(gatehouse_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="gatehouse not found.")
    
    # Gửi dữ liệu cập nhật cho app Android có địa chỉ IP cụ thể
    target_ip = "192.168.1.8"  # Địa chỉ IP cần gửi dữ liệu
    await send_json_to_android_app(target_ip, gatehouse_update)
    
    return gatehouse_service.update_gatehouse(gatehouse_document_ID, gatehouse_update)

async def send_json_to_android_app(ip: str, json_data: dict):
    url = f"http://{ip}/endpoint"  # Đường dẫn endpoint của app Android
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=json_data)
            
            if response.status_code == 200:
                print("Dữ liệu đã được gửi thành công tới app Android.")
            else:
                raise HTTPException(status_code=response.status_code, detail="Gửi dữ liệu tới app Android không thành công.")
    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=f"Lỗi khi gửi dữ liệu tới app Android: {exc}")










# from fastapi import APIRouter, Body, HTTPException
# from fastapi import WebSocket
# from fastapi.responses import JSONResponse
# from schemas.gatehouse_schema import GateHouse
# from typing import Dict
# from services.gatehouse_service import GatehouseService
# gatehouse_service = GatehouseService()

# router = APIRouter()
# connected_clients: Dict[str, WebSocket] = {}  # Sử dụng dict để lưu trữ các client kết nối

# @router.put("/gatehouse/home/update/{gatehouse_document_ID}", response_model=GateHouse, tags=["gatehouse"])
# async def update_gatehouse(websocket: WebSocket, gatehouse_document_ID: str, gatehouse_update: GateHouse = Body(...)) -> GateHouse:
#     result = gatehouse_service.get_gatehouse(gatehouse_document_ID)
#     if not result:
#         raise HTTPException(status_code=404, detail="gatehouse not found.")

#     # Lưu trữ client WebSocket theo địa chỉ IP
#     connected_clients[websocket.client.host] = websocket

#     # Gửi dữ liệu cập nhật cho client app Android có địa chỉ IP cụ thể
#     target_ip = "27.69.146.73"  # Địa chỉ IP cần gửi dữ liệu
#     if target_ip in connected_clients:
#         target_client = connected_clients[target_ip]
#         await target_client.send_json(gatehouse_update.dict())

#     return gatehouse_service.update_gatehouse(gatehouse_document_ID, gatehouse_update)

# @router.put("/gatehouse/app/update/{gatehouse_document_ID}", response_model=GateHouse, tags=["gatehouse"])
# async def update_gatehouse(websocket: WebSocket, gatehouse_document_ID: str, gatehouse_update: GateHouse = Body(...)) -> GateHouse:
#     result = gatehouse_service.get_gatehouse(gatehouse_document_ID)
#     if not result:
#         raise HTTPException(status_code=404, detail="gatehouse not found.")

#     # Lưu trữ client WebSocket theo địa chỉ IP
#     connected_clients[websocket.client.host] = websocket

#     # Gửi dữ liệu cập nhật cho client app Android có địa chỉ IP cụ thể
#     target_ip = "192.168.1.8"  # Địa chỉ IP cần gửi dữ liệu
#     if target_ip in connected_clients:
#         target_client = connected_clients[target_ip]
#         await target_client.send_json(gatehouse_update.dict())

#     return gatehouse_service.update_gatehouse(gatehouse_document_ID, gatehouse_update)
