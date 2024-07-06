import uuid
from middlewares.exception import ValidationException
from models.commonModel import Login
from constants import USER_BUSINESS_VALIDATION_GET_BY_ID_CODE, USER_BUSINESS_VALIDATION_GET_BY_ID_MSG, USER_BUSINESS_VALIDATION_LOGIN_PASSWORD_CODE, USER_BUSINESS_VALIDATION_LOGIN_PASSWORD_MSG, USER_BUSINESS_VALIDATION_LOGIN_USERNAME_CODE, USER_BUSINESS_VALIDATION_LOGIN_USERNAME_MSG


def getByIdValidation(id: uuid.UUID):
    if id == "":
        raise ValidationException(
            USER_BUSINESS_VALIDATION_GET_BY_ID_MSG, USER_BUSINESS_VALIDATION_GET_BY_ID_CODE)


def loginValidation(model: Login):
    if model.userName.strip() == "":
        raise ValidationException(
            USER_BUSINESS_VALIDATION_LOGIN_USERNAME_MSG, USER_BUSINESS_VALIDATION_LOGIN_USERNAME_CODE)
    if model.password.strip() == "":
        raise ValidationException(
            USER_BUSINESS_VALIDATION_LOGIN_PASSWORD_MSG, USER_BUSINESS_VALIDATION_LOGIN_PASSWORD_CODE)
