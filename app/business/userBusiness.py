"""Business Module"""
from sqlalchemy.orm import Session
from middlewares.exception import BusinessException
from core.authentication import createToken, hashPassword, verifyPassword
from business.iUserBusiness import IUserBusiness
from business.userBusinessValidation import *
from services.userService import UserService
from models.serviceResult import ServiceResult, ServicePaginationResult
from models.dtos.userDto import UserDto, UserLoginDto
from models.commonModel import Token, PaginationQuery, ResponseModel, ResponsePaginationModel
from constants import LOGIC_GET_ALL_ERROR_CODE, LOGIC_HARD_DELETE_CODE, LOGIC_HARD_DELETE_ERROR_CODE, LOGIC_LOGIN_ERROR_CODE, LOGIC_LOGIN_GET_BY_ID_CODE, LOGIC_LOGIN_INCORRECT_INFO_CODE, LOGIC_REGISTER_ERROR_CODE, LOGIC_SOFT_DELETE_CODE, LOGIC_SOFT_DELETE_ERROR_CODE, LOGIC_UPDATE_CODE, LOGIC_UPDATE_ERROR_CODE


class UserBusiness(IUserBusiness):

    def login(model: Login, db: Session) -> ResponseModel[Token]:
        tlr = Translator()
        loginValidation(model)
        try:
            result: ServiceResult[UserLoginDto] = UserService.login(model.userName, db) #fmt:off
            #fmt:on
            if result.isSuccess == False:
                raise BusinessException(
                    tlr.t('exception.logic_login_incorrect_info'), LOGIC_LOGIN_INCORRECT_INFO_CODE)

            checkPassword = verifyPassword(
                model.password, result.data.hashedPassword)

            if checkPassword == False:
                raise BusinessException(
                    tlr.t('exception.logic_login_incorrect_info'), LOGIC_LOGIN_INCORRECT_INFO_CODE)

            token = createToken(
                data={
                    "userId": str(result.data.id),
                    "userName": result.data.email,
                    "role": "admin",
                }
            )
            return ResponseModel[Token](data=Token(token=token))
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                tlr.t('exception.logic_login_error'), LOGIC_LOGIN_ERROR_CODE)

    def register(model: UserDto, db: Session) -> ResponseModel[UserDto]:
        tlr = Translator()
        try:
            model.hashedPassword = hashPassword(model.hashedPassword)
            result: ServiceResult[UserDto] = UserService.register(model, db)
            return ResponseModel[UserDto](data=result.data)
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                tlr.t('exception.logic_register_error'), LOGIC_REGISTER_ERROR_CODE)

    def getById(id: str, db: Session) -> ResponseModel[UserDto]:
        getByIdValidation(id)
        tlr = Translator()
        try:
            result: ServiceResult[UserDto] = UserService.getById(id, db)
            if result.isSuccess == False:
                raise BusinessException(
                    tlr.t('exception.logic_login_get_by_id'), LOGIC_LOGIN_GET_BY_ID_CODE)
            return ResponseModel[UserDto](data=result.data)
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                tlr.t('exception.logic_login_error'), LOGIC_LOGIN_ERROR_CODE)

    def getAll(p: PaginationQuery, q: list[str], db: Session) -> ResponsePaginationModel[list[UserDto]]:
        tlr = Translator()
        try:
            result: ServicePaginationResult[list[UserDto]] = UserService.getAll(
                p, q, db)
            return ResponsePaginationModel[list[UserDto]](
                data=result.data, total=result.total, pages=result.pages, page=result.page, size=result.size)
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                tlr.t('exception.logic_get_all_error'), LOGIC_GET_ALL_ERROR_CODE)

    def update(id: str, model: UserDto, db: Session) -> ResponseModel[UserDto]:
        tlr = Translator()
        try:
            result: ServiceResult[UserDto] = UserService.update(id, model, db)
            if result.isSuccess == False:
                raise BusinessException(
                    tlr.t('exception.logic_update'), LOGIC_UPDATE_CODE)
            return ResponseModel[UserDto](data=result.data)
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                tlr.t('exception.logic_update_error'), LOGIC_UPDATE_ERROR_CODE)

    def softDelete(id: str, db: Session) -> ResponseModel[bool]:
        tlr = Translator()
        try:
            result: ServiceResult[UserDto] = UserService.softDelete(id, db)
            if result.isSuccess == False:
                raise BusinessException(
                    tlr.t('exception.logic_soft_delete'), LOGIC_SOFT_DELETE_CODE)
            return ResponseModel[bool](data=result.data)
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                tlr.t('exception.logic_soft_delete_error'), LOGIC_SOFT_DELETE_ERROR_CODE)

    def hardDelete(id: str, db: Session) -> ResponseModel[bool]:
        tlr = Translator()
        try:
            result: ServiceResult[UserDto] = UserService.hardDelete(id, db)
            if result.isSuccess == False:
                raise BusinessException(
                    tlr.t('exception.logic_hard_delete'), LOGIC_HARD_DELETE_CODE)
            return ResponseModel[bool](data=result.data)
        except BusinessException:
            raise
        except Exception:
            raise BusinessException(
                tlr.t('exception.logic_hard_delete_error'), LOGIC_HARD_DELETE_ERROR_CODE)
