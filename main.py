import uvicorn
from typing import Any, Callable

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from routers import camera_router

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
# if __name__=="__main__":
#     uvicorn.run(app, port=10000, host="0.0.0.0")