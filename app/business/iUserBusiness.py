"""Interface class module."""

import uuid
from abc import ABCMeta, abstractmethod
from sqlalchemy.orm import Session
from models.commonModel import Login, Token
from models.dtos.userDto import UserDto


class IUserBusiness(metaclass=ABCMeta):

    @abstractmethod
    def login(model: Login, db: Session) -> Token: ...

    @abstractmethod
    def register(model: UserDto, db: Session) -> UserDto: ...

    @abstractmethod
    def getById(id: str, db: Session) -> UserDto: ...

    @abstractmethod
    def getAll(db: Session) -> list[UserDto]: ...

    @abstractmethod
    def update(id: str, model: UserDto, db: Session) -> UserDto: ...

    @abstractmethod
    def softDelete(id: str, db: Session) -> bool: ...

    @abstractmethod
    def hardDelete(id: str, db: Session) -> bool: ...
