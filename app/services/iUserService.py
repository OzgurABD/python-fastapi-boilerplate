"""Interface class module."""

from abc import ABCMeta, abstractmethod
from models.serviceResult import ServiceResult
from database.dbModels import User


class IUserService(metaclass=ABCMeta):

    @abstractmethod
    def login(email: str, hashedPassword: str) -> ServiceResult[User]: ...

    @abstractmethod
    def register(model: User) -> ServiceResult[User]: ...

    @abstractmethod
    def forgotPassword(email: str) -> ServiceResult[User]: ...

    @abstractmethod
    def getById(id: str) -> ServiceResult[User]: ...

    @abstractmethod
    def getByEmail(email: str) -> ServiceResult[User]: ...

    @abstractmethod
    def getAll() -> ServiceResult[list[User]]: ...

    @abstractmethod
    def update(model: User) -> ServiceResult[User]: ...

    @abstractmethod
    def delete(id: str) -> ServiceResult[User]: ...
