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


class PaginationQuery(BaseModel):
    page: int | None = 1
    size: int | None = 25
    order: str | None = "cDate"


class PaginationModel(BaseModel):
    total: int | None = None
    pages: int | None = None
    page: int | None = None
    size: int | None = None


class ResponseModel(BaseModel, Generic[T]):
    data: Optional[T] | None = None


class ResponsePaginationModel(BaseModel, ResponseModel):
    total: int | None = None
    pages: int | None = None
    page: int | None = None
    size: int | None = None


class Message(BaseModel):
    message: str | None = None
