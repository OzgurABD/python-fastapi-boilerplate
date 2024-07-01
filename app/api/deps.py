from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from dependency_injector.wiring import Provide
from database.dbSession import getDbSession
from models.commonModel import TokenPayload
from core.authentication import contextUser
from api.containers import Container

DbSessionDep = Annotated[Session, Depends(getDbSession)]
CurrentUserDep = Annotated[TokenPayload, Depends(contextUser)]

UserServiceDep = Depends(Provide[Container.userService])
