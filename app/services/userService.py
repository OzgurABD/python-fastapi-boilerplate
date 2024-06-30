"""Services module."""

from sqlalchemy import select
from core.deps import DbSessionDep
from .iUserService import IUserService
from database.dbModels import User
from models.serviceResult import ServiceResult
from models.dtos.userDto import UserDto


@IUserService.register
class UserService:

    def login(email: str, hashedPassword: str) -> ServiceResult[UserDto]:
        user = None
        return ServiceResult[UserDto](data=user, success=True)

    def register(model: User) -> ServiceResult[UserDto]: ...

    def forgotPassword(email: str) -> ServiceResult[UserDto]: ...

    def getById(id: str) -> ServiceResult[UserDto]: ...

    def getByEmail(email: str) -> ServiceResult[UserDto]: ...

    def getAll() -> ServiceResult[list[UserDto]]:
        result =  DbSessionDep.execute(select(User))  
        return ServiceResult[list[UserDto]]()

    def update(model: User) -> ServiceResult[UserDto]: ...

    def delete(id: str) -> ServiceResult[UserDto]: ...
