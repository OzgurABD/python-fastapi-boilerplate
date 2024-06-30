"""Services module."""

from sqlalchemy.exc import IntegrityError
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

    def register(model: UserDto) -> ServiceResult[UserDto]:
        try:
            userEntity: User = None
            DbSessionDep.add(userEntity)
            DbSessionDep.commit()
        except IntegrityError as e:
            DbSessionDep.rollback()

    def forgotPassword(email: str) -> ServiceResult[UserDto]: ...

    def getById(id: str) -> ServiceResult[UserDto]:
        result = DbSessionDep.query(User).filter_by(id=id).first()
        return ServiceResult[UserDto](data=result, isSuccess=result != None)
        # TODO Dont Forget session.close() structure

    def getByEmail(email: str) -> ServiceResult[UserDto]: ...

    def getAll() -> ServiceResult[list[UserDto]]:
        result = DbSessionDep.query(User).all()
        return ServiceResult[list[UserDto]](data=result, isSuccess=len(result) > 0)

    def update(model: UserDto) -> ServiceResult[UserDto]: ...

    def delete(id: str) -> ServiceResult[UserDto]: ...
