import uuid
from middlewares.exception import ValidationException
from models.commonModel import Login


def getByIdValidation(id: uuid.UUID):
    if id == "":
        raise ValidationException("Id boş olamaz.", "UGBIV.0001")


def loginValidation(model: Login):
    if model.userName.strip() == "":
        raise ValidationException("UserName boş olamaz.", "ULV.0001")
    if model.password.strip() == "":
        raise ValidationException("Password boş olamaz.", "ULV.0002")
