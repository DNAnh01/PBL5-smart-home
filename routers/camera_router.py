from fastapi import APIRouter, Body, HTTPException
from services.camera_service import CameraService
from schemas.camera_schema import Camera

import datetime
import pytz


router = APIRouter()
camera_service = CameraService()

@router.post("/camera/create", response_model=Camera, tags=["camera"])
async def create_camera(camera_create: Camera = Body(...)) -> Camera:
    return camera_service.create_camera(camera_create)

@router.get("/camera/get/{camera_document_ID}", response_model=Camera, tags=["camera"])
async def get_camera(camera_document_ID: str) -> Camera:
    result = camera_service.get_camera(camera_document_ID)
    if not result:
        raise HTTPException(status_code=404, detail="camera not found.")
    return result

@router.put("/camera/update/{camera_document_ID}", response_model=Camera, tags=["camera"])
async def update_camera(camera_document_ID: str, camera_update: Camera = Body(...)) -> Camera:
    result = camera_service.get_camera(camera_document_ID)
    camera_update.timestamp = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime("%d-%m-%Y %H:%M:%S")
    if not result:
        raise HTTPException(status_code=404, detail="camera not found.")
    return camera_service.update_camera(camera_document_ID, camera_update)

