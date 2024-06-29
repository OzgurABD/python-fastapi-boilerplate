import uuid
from pydantic import BaseModel


class UserRegisterDto(BaseModel):
    email: str
    fullName: str
    phoneNumber: str | None = None


class UserDto(BaseModel):
    id: uuid.UUID
    email: str
    fullName: str
    phoneNumber: str | None = None
