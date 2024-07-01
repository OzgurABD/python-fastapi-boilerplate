import uuid
from pydantic import BaseModel


class User(BaseModel):
    id: uuid.UUID
    email: str
    fullName: str
    phoneNumber: str | None = None


class UserResponseModel(BaseModel):
    data: User


class UsersResponseModel(BaseModel):
    data: list[User]
