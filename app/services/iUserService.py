"""Interface class module."""

from abc import ABCMeta, abstractmethod
from models.serviceResult import ServiceResult
from models.dtos.userDto import UserDto

class IUserService(metaclass=ABCMeta):

    @abstractmethod
    def login(email: str, hashedPassword: str) -> ServiceResult[UserDto]: ...

    @abstractmethod
    def register(model: UserDto) -> ServiceResult[UserDto]: ...

    @abstractmethod
    def forgotPassword(email: str) -> ServiceResult[UserDto]: ...

    @abstractmethod
    def getById(id: str) -> ServiceResult[UserDto]: ...

    @abstractmethod
    def getByEmail(email: str) -> ServiceResult[UserDto]: ...

    @abstractmethod
    def getAll() -> ServiceResult[list[UserDto]]: ...

    @abstractmethod
    def update(model: UserDto) -> ServiceResult[UserDto]: ...

    @abstractmethod
    def delete(id: str) -> ServiceResult[UserDto]: ...
