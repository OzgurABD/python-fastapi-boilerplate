from fastapi import APIRouter
from app.api.routes.v1 import plate

api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
api_router.include_router(plate.router, prefix="/plate", tags=["plate"])
