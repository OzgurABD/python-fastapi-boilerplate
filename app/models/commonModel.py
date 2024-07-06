from typing import Generic, Optional
from annotated_types import T
from pydantic import BaseModel


class Token(BaseModel):
    token: str
    tokenType: str | None = "bearer"


class TokenPayload(BaseModel):
    userId: str | None = None
    userName: str | None = None
    role: str | None = None


class Login(BaseModel):
    userName: str | None = None
    password: str | None = None


class PaginateModel(BaseModel, Generic[T]):
    data: Optional[T]
    pageNumber: int
    pageSize: int
    totalCount: int


class Message(BaseModel):
    message: str | None = None
