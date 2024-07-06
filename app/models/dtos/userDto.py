import uuid
from pydantic import BaseModel


class UserLoginDto(BaseModel):
    id: uuid.UUID | None = None
    hashedPassword: str | None = None
    email: str | None = None
    identityNumber: str | None = None


class UserDto(BaseModel):
    id: uuid.UUID | None = None
    email: str | None = None
    hashedPassword: str | None = None
    identityNumber: str | None = None
    fullName: str | None = None
    phoneNumber: str | None = None
    birthday: str | None = None
