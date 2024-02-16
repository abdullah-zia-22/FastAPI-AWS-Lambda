from fastapi import APIRouter

from app.api.v1.endpoints import (
task
)

api_router = APIRouter()

api_router.include_router(
    task.router,
    prefix="/task",
    tags=["Tasks"]
)