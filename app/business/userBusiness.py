"""Business Module"""
from sqlalchemy.orm import Session
from middlewares.exception import BusinessException
from core.authentication import createToken, hashPassword, verifyPassword
from business.iUserBusiness import IUserBusiness
from business.userBusinessValidation import *
from services.userService import UserService
from models.serviceResult import ServiceResult
from models.dtos.userDto import UserDto, UserLoginDto
from models.commonModel import Token
from constants import USER_BUSINESS_LOGIC_GET_ALL_ERROR_CODE, USER_BUSINESS_LOGIC_GET_ALL_ERROR_MSG, USER_BUSINESS_LOGIC_HARD_DELETE_CODE, USER_BUSINESS_LOGIC_HARD_DELETE_ERROR_CODE, USER_BUSINESS_LOGIC_HARD_DELETE_ERROR_MSG, USER_BUSINESS_LOGIC_HARD_DELETE_MSG, USER_BUSINESS_LOGIC_LOGIN_ERROR_CODE, USER_BUSINESS_LOGIC_LOGIN_ERROR_MSG, USER_BUSINESS_LOGIC_LOGIN_GET_BY_ID_CODE, USER_BUSINESS_LOGIC_LOGIN_GET_BY_ID_MSG, USER_BUSINESS_LOGIC_LOGIN_INCORRECT_INFO_CODE, USER_BUSINESS_LOGIC_LOGIN_INCORRECT_INFO_MSG, USER_BUSINESS_LOGIC_REGISTER_ERROR_CODE, USER_BUSINESS_LOGIC_REGISTER_ERROR_MSG, USER_BUSINESS_LOGIC_SOFT_DELETE_CODE, USER_BUSINESS_LOGIC_SOFT_DELETE_ERROR_CODE, USER_BUSINESS_LOGIC_SOFT_DELETE_ERROR_MSG, USER_BUSINESS_LOGIC_SOFT_DELETE_MSG, USER_BUSINESS_LOGIC_UPDATE_CODE, USER_BUSINESS_LOGIC_UPDATE_ERROR_CODE, USER_BUSINESS_LOGIC_UPDATE_ERROR_MSG, USER_BUSINESS_LOGIC_UPDATE_MSG


class UserBusiness(IUserBusiness):

    def login(model: Login, db: Session) -> Token:
        loginValidation(model)
        try:
            result: ServiceResult[UserLoginDto] = UserService.login(model.userName, db) #fmt:off
            #fmt:on
            if result.isSuccess == False:
                raise BusinessException(
                    USER_BUSINESS_LOGIC_LOGIN_INCORRECT_INFO_MSG, USER_BUSINESS_LOGIC_LOGIN_INCORRECT_INFO_CODE)

            checkPassword = verifyPassword(
                model.password, result.data.hashedPassword)

            if checkPassword == False:
                raise BusinessException(
                    USER_BUSINESS_LOGIC_LOGIN_INCORRECT_INFO_MSG, USER_BUSINESS_LOGIC_LOGIN_INCORRECT_INFO_CODE)

            token = createToken(
                data={
                    "userId": str(result.data.id),
                    "userName": result.data.email,
                    "role": "admin",
                }
            )
            return Token(token=token)
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                USER_BUSINESS_LOGIC_LOGIN_ERROR_MSG, USER_BUSINESS_LOGIC_LOGIN_ERROR_CODE)

    def register(model: UserDto, db: Session) -> UserDto:
        try:
            model.hashedPassword = hashPassword(model.hashedPassword)
            result: ServiceResult[UserDto] = UserService.register(model, db)
            return result.data
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                USER_BUSINESS_LOGIC_REGISTER_ERROR_MSG, USER_BUSINESS_LOGIC_REGISTER_ERROR_CODE)

    def getById(id: str, db: Session) -> UserDto:
        getByIdValidation(id)
        try:
            result: ServiceResult[UserDto] = UserService.getById(id, db)
            if result.isSuccess == False:
                raise BusinessException(
                    USER_BUSINESS_LOGIC_LOGIN_GET_BY_ID_MSG, USER_BUSINESS_LOGIC_LOGIN_GET_BY_ID_CODE)
            return result.data
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                USER_BUSINESS_LOGIC_LOGIN_ERROR_MSG, USER_BUSINESS_LOGIC_LOGIN_ERROR_CODE)

    def getAll(db: Session) -> list[UserDto]:
        try:
            result: ServiceResult[list[UserDto]] = UserService.getAll(db)
            return result.data
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                USER_BUSINESS_LOGIC_GET_ALL_ERROR_MSG, USER_BUSINESS_LOGIC_GET_ALL_ERROR_CODE)

    def update(id: str, model: UserDto, db: Session) -> UserDto:
        try:
            result: ServiceResult[UserDto] = UserService.update(id, model, db)
            if result.isSuccess == False:
                raise BusinessException(
                    USER_BUSINESS_LOGIC_UPDATE_MSG, USER_BUSINESS_LOGIC_UPDATE_CODE)
            return result.data
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                USER_BUSINESS_LOGIC_UPDATE_ERROR_MSG, USER_BUSINESS_LOGIC_UPDATE_ERROR_CODE)

    def softDelete(id: str, db: Session) -> bool:
        try:
            result: ServiceResult[UserDto] = UserService.softDelete(id, db)
            if result.isSuccess == False:
                raise BusinessException(
                    USER_BUSINESS_LOGIC_SOFT_DELETE_MSG, USER_BUSINESS_LOGIC_SOFT_DELETE_CODE)
            return result.data
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                USER_BUSINESS_LOGIC_SOFT_DELETE_ERROR_MSG, USER_BUSINESS_LOGIC_SOFT_DELETE_ERROR_CODE)

    def hardDelete(id: str, db: Session) -> bool:
        try:
            result: ServiceResult[UserDto] = UserService.hardDelete(id, db)
            if result.isSuccess == False:
                raise BusinessException(
                    USER_BUSINESS_LOGIC_HARD_DELETE_MSG, USER_BUSINESS_LOGIC_HARD_DELETE_CODE)
            return result.data
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                USER_BUSINESS_LOGIC_HARD_DELETE_ERROR_MSG, USER_BUSINESS_LOGIC_HARD_DELETE_ERROR_CODE)
