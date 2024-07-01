from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from database.dbSession import getDbSession
from models.commonModel import TokenPayload
from core.authentication import contextUser

DbSessionDep = Annotated[Session, Depends(getDbSession)]
CurrentUserDep = Annotated[TokenPayload, Depends(contextUser)]
