from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from database.session import dbSession
from models.commonModel import TokenPayload
from core.authentication import contextUser


async def commonParams(page: int | None = 1, size: int | None = 25, order: str | None = "cDate"):
    return {"page": page, "size": size, "order": order}

DbSessionDep: Session = Depends(dbSession)
CurrentUserDep: TokenPayload = Depends(contextUser)
CommonParamsDep: dict = Depends(commonParams)
