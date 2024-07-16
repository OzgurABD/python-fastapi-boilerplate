import uuid
from lang.translator import Translator
from middlewares.exception import ValidationException
from models.commonModel import Login
from constants import VALIDATION_GET_BY_ID_CODE, VALIDATION_LOGIN_PASSWORD_CODE, VALIDATION_LOGIN_USERNAME_CODE


def getByIdValidation(id: uuid.UUID):
    tlr = Translator()
    if id == "":
        raise ValidationException(
            tlr.t('exception.validation_get_by_id'), VALIDATION_GET_BY_ID_CODE)


def loginValidation(model: Login):
    tlr = Translator()
    if model.userName.strip() == "":
        raise ValidationException(
            tlr.t('exception.validation_login_username'), VALIDATION_LOGIN_USERNAME_CODE)
    if model.password.strip() == "":
        raise ValidationException(
            tlr.t('exception.validation_login_password'), VALIDATION_LOGIN_PASSWORD_CODE)
