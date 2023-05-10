import uvicorn
from typing import Any, Callable

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from fastapi.openapi.utils import get_openapi

from routers import (camera_router, 
                     notice_details_router,
                     notice_details_view_router,
                     sensors_router,
                     sensors_view_router,
                     gatehouse_router,
                     led_router,
                     dc_router,
                     test_ws)

app = FastAPI()

'''
    middleware
'''
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

'''
    Routers
'''



app.include_router(camera_router.router)
app.include_router(notice_details_router.router)
app.include_router(notice_details_view_router.router)
app.include_router(sensors_router.router)
app.include_router(sensors_view_router.router)
app.include_router(gatehouse_router.router)
app.include_router(led_router.router)
app.include_router(dc_router.router)
app.include_router(test_ws.router)
