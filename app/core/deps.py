from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from database.dbSession import getDbSession
from models.baseModel import TokenPayload
from core.authentication import contextUser


# from dependency_injector import containers, providers
# from dependency_injector.wiring import Provide, inject


DbSessionDep = Annotated[Session, Depends(getDbSession)]
CurrentUserDep = Annotated[TokenPayload, Depends(contextUser)]


# class Service:
#     async def process(self) -> str:
#         return "OK"

# class Container(containers.DeclarativeContainer):
#     service = providers.Factory(Service)

# app = FastAPI()

# @app.api_route("/")
# @inject
# async def index(service: Service = Depends(Provide[Container.service])):
#     result = await service.process()
#     return {"result": result}


# container = Container()
# container.wire(modules=[__name__])


# https://github.com/ets-labs/python-dependency-injector/blob/master/examples/miniapps/application-multiple-containers/example/__main__.py
