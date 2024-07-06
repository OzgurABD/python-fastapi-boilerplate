from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from database.session import dbSession
from models.commonModel import TokenPayload
from core.authentication import contextUser

DbSessionDep: Session = Depends(dbSession)
CurrentUserDep: TokenPayload = Depends(contextUser)
