"""Services module."""
from sqlalchemy import desc
from sqlalchemy.orm import Session
from .iUserService import IUserService
from database.entities.user import User
from models.serviceResult import ServiceResult, ServicePaginationResult
from models.dtos.userDto import UserDto, UserLoginDto
from mappers.mapToDto.userDtoMapper import MapUserEntityToUserDto, MapUsersEntityToUsersDto, MapUserEntityToUserLoginDto


class UserService(IUserService):

    def login(email: str, db: Session) -> ServiceResult[UserLoginDto]:
        result: User = db.query(User).filter_by(email=email).first()
        _data = None if result == None else MapUserEntityToUserLoginDto(result)
        return ServiceResult[UserLoginDto](data=_data, isSuccess=result != None)

    def register(model: UserDto, db: Session) -> ServiceResult[UserDto]:
        entity = User(
            hashedPassword=model.hashedPassword,
            email=model.email,
            identityNumber=model.identityNumber,
            fullName=model.fullName,
            phoneNumber=model.phoneNumber,
            birthday=model.birthday)
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return ServiceResult[UserDto](data=UserDto(id=entity.id), isSuccess=True)

    def forgotPassword(email: str, db: Session) -> ServiceResult[UserDto]: ...

    def getById(id: str, db: Session) -> ServiceResult[UserDto]:
        result: User = db.query(User).filter_by(id=id).first()
        _data = None if result == None else MapUserEntityToUserDto(result)
        return ServiceResult[UserDto](data=_data, isSuccess=_data != None)

    def getByEmail(email: str, db: Session) -> ServiceResult[UserDto]:
        result: User = db.query(User).filter_by(email=email).first()
        _data = None if result == None else MapUserEntityToUserDto(result)
        return ServiceResult[UserDto](data=_data, isSuccess=_data != None)

    def getAll(params: dict, db: Session) -> ServicePaginationResult[list[UserDto]]:
        _query = db.query(User)

        if params["email"]:
            _query = _query.filter_by(email=params["email"])

        if params["orderType"] == "desc":
            _query = _query.order_by(desc(params["orderBy"]))
        else:
            _query = _query.order_by(params["orderBy"])

        _count = _query.count()
        result: list[User] = _query.slice(
            (params["page"]-1)*params["size"], params["page"]*params["size"]).all()

        _data = None if result == None else MapUsersEntityToUsersDto(result)

        return ServicePaginationResult[list[UserDto]](
            data=_data, isSuccess=len(_data) > 0, total=_count, pages=int(_count/params["size"])+1, page=params["page"], size=params["size"])

    def update(id: str, model: UserDto, db: Session) -> ServiceResult[UserDto]:
        result: User = db.query(User).filter(User.id == id).first()
        if not result:
            return ServiceResult(isSuccess=False)
        result.email = model.email
        result.identityNumber = model.identityNumber
        result.fullName = model.fullName
        result.phoneNumber = model.phoneNumber
        result.birthday = model.birthday
        db.commit()
        _data = MapUserEntityToUserDto(result)
        return ServiceResult[UserLoginDto](data=_data, isSuccess=True)

    def softDelete(id: str, db: Session) -> ServiceResult[UserDto]:
        result: User = db.query(User).filter(User.id == id).first()
        if not result:
            return ServiceResult(isSuccess=False)
        result.isDelete = True
        db.commit()
        return ServiceResult(isSuccess=True)

    def hardDelete(id: str, db: Session) -> ServiceResult[UserDto]:
        result = db.query(User).filter(User.id == id).first()
        if not result:
            return ServiceResult(isSuccess=False)
        db.delete(result)
        db.commit()
        return ServiceResult(isSuccess=True)
