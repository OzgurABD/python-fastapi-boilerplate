from fastapi import APIRouter
from api.routers.v1 import userRouter

apiRouter = APIRouter()
apiRouter.include_router(userRouter.router, prefix="/user", tags=["user"])
