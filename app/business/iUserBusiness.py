"""Interface class module."""

from abc import ABCMeta, abstractmethod
from sqlalchemy.orm import Session
from models.commonModel import Login, Token, ResponseModel, ResponsePaginationModel
from models.dtos.userDto import UserDto


class IUserBusiness(metaclass=ABCMeta):

    @abstractmethod
    def login(model: Login, db: Session) -> ResponseModel[Token]: ...

    @abstractmethod
    def register(model: UserDto, db: Session) -> ResponseModel[UserDto]: ...

    @abstractmethod
    def getById(id: str, db: Session) -> ResponseModel[UserDto]: ...

    @abstractmethod
    def getAll(params:dict, db: Session) -> ResponsePaginationModel[list[UserDto]]: ... #fmt:off

    @abstractmethod
    def update(id: str, model: UserDto, db: Session) -> ResponseModel[UserDto]: ...

    @abstractmethod
    def softDelete(id: str, db: Session) -> ResponseModel[bool]: ...

    @abstractmethod
    def hardDelete(id: str, db: Session) -> ResponseModel[bool]: ...
