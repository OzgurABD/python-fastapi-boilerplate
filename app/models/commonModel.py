from typing import Generic, Optional
from annotated_types import T
from pydantic import BaseModel


class Token(BaseModel):
    token: str
    tokenType: str = "bearer"


class TokenPayload(BaseModel):
    userId: str | None = None
    userName: str | None = None
    roles: list | None = None


class Login(BaseModel):
    userName: str
    password: str


class PaginateModel(BaseModel, Generic[T]):
    data: Optional[T]
    pageNumber: int
    pageSize: int
    totalCount: int


class Message(BaseModel):
    message: str
