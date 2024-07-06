import uuid
from pydantic import BaseModel


class UserModel(BaseModel):
    id: uuid.UUID | None = None
    email: str | None = None
    fullName: str | None = None
    phoneNumber: str | None = None


class UserResponseModel(BaseModel):
    data: UserModel


class UsersResponseModel(BaseModel):
    data: list[UserModel]
