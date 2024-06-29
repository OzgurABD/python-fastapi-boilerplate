"""Interface class module."""

import uuid
from abc import ABCMeta, abstractmethod
from models.baseModel import Login, Token
from models.dtos.userDto import UserRegisterDto
from models.responses.userResponseModel import UserResponseModel, UsersResponseModel


class IUserBusiness(metaclass=ABCMeta):

    @abstractmethod
    def login(model: Login) -> Token: ...

    @abstractmethod
    def getById(id: uuid.UUID) -> UserResponseModel: ...

    @abstractmethod
    def getAll() -> UsersResponseModel: ...

    @abstractmethod
    def register(model: UserRegisterDto) -> UsersResponseModel: ...
