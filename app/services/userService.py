"""Services module."""

from sqlalchemy.exc import IntegrityError
from api.deps import DbSessionDep
from .iUserService import IUserService
from database.entities.user import User
from models.serviceResult import ServiceResult
from models.dtos.userDto import UserDto


@IUserService.register
class UserService:

    def login(email: str, hashedPassword: str) -> ServiceResult[UserDto]:
        result = DbSessionDep.query(User).filter_by(
            email=email, hashedPassword=hashedPassword).first()
        return ServiceResult[UserDto](data=result, success=result != None)

    def register(model: UserDto) -> ServiceResult[UserDto]:
        userEntity: User = None
        DbSessionDep.add(userEntity)
        DbSessionDep.commit()
        DbSessionDep.refresh(userEntity)
        return ServiceResult[UserDto](data=userEntity, isSuccess=True)

    def forgotPassword(email: str) -> ServiceResult[UserDto]: ...

    def getById(id: str) -> ServiceResult[UserDto]:
        result = DbSessionDep.query(User).filter_by(id=id).first()
        return ServiceResult[UserDto](data=result, isSuccess=result != None)
        # TODO Dont Forget session.close() structure

    def getByEmail(email: str) -> ServiceResult[UserDto]:
        result = DbSessionDep.query(User).filter_by(email=email).first()
        return ServiceResult[UserDto](data=result, isSuccess=result != None)

    def getAll() -> ServiceResult[list[UserDto]]:
        result = DbSessionDep.query(User).all()
        return ServiceResult[list[UserDto]](data=result, isSuccess=len(result) > 0)

    def update(model: UserDto) -> ServiceResult[UserDto]: ...

    def delete(id: str) -> ServiceResult[UserDto]:
        result = DbSessionDep.query(User).filter(User.id == id).first()
        if not result:
            return ServiceResult(isSuccess=False)
        DbSessionDep.delete(result)
        DbSessionDep.commit()
        return ServiceResult(isSuccess=True)
