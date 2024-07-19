import uuid
from pydantic import BaseModel
from models.commonModel import ResponsePaginationModel


class UserModel(BaseModel):
    id: uuid.UUID | None = None
    email: str | None = None
    fullName: str | None = None
    phoneNumber: str | None = None


class UserResponseModel(BaseModel):
    data: UserModel


class UsersResponseModel(ResponsePaginationModel):
    data: list[UserModel]
