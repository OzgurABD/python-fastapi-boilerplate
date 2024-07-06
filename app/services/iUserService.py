"""Interface class module."""

from abc import ABCMeta, abstractmethod
from sqlalchemy.orm import Session
from models.serviceResult import ServiceResult
from models.dtos.userDto import UserDto, UserLoginDto


class IUserService(metaclass=ABCMeta):

    @abstractmethod
    def login(email: str, db: Session) -> ServiceResult[UserLoginDto]: ... #fmt:off

    @abstractmethod
    def register(model: UserDto, db: Session) -> ServiceResult[UserDto]: ...

    @abstractmethod
    def forgotPassword(email: str, db: Session) -> ServiceResult[UserDto]: ...

    @abstractmethod
    def getById(id: str, db: Session) -> ServiceResult[UserDto]: ...

    @abstractmethod
    def getByEmail(email: str, db: Session) -> ServiceResult[UserDto]: ...

    @abstractmethod
    def getAll(db: Session) -> ServiceResult[list[UserDto]]: ...

    @abstractmethod
    def update(id: str, model: UserDto, db: Session) -> UserDto: ...

    @abstractmethod
    def softDelete(id: str, db: Session) -> bool: ...

    @abstractmethod
    def hardDelete(id: str, db: Session) -> bool: ...

