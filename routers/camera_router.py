from fastapi import APIRouter, Body, HTTPException
from services.camera_service import CameraService
from schemas.camera_schema import Camera

router = APIRouter()
camera_service = CameraService()


@router.post("/camera/create", response_model=Camera, tags=["camera"])
async def create_camera(camera_create: Camera = Body(...)) -> Camera:
    return camera_service.create_camera(camera_create)


@router.get("/camera/get", response_model=Camera, tags=["camera"])
async def get_camera() -> Camera:
    result = camera_service.get_camera()
    if not result:
        raise HTTPException(status_code=404, detail="camera not found.")
    return result

@router.put("camera/update", response_model=Camera, tags=["camera"])
async def update_camera(camera_update: Camera = Body(...)) -> Camera:
    return camera_service.update_camera(camera_update)

