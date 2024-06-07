from fastapi import APIRouter
from api.routers.v1 import plateRouter

apiRouter = APIRouter()
# api_router.include_router(login.router, tags=["login"])
apiRouter.include_router(plateRouter.router, prefix="/plate", tags=["plate"])
