from fastapi import APIRouter
from api.routers.v1 import plateRouter, authRouter

apiRouter = APIRouter()
apiRouter.include_router(authRouter.router, prefix="/auth", tags=["auth"])
apiRouter.include_router(plateRouter.router, prefix="/plate", tags=["plate"])
