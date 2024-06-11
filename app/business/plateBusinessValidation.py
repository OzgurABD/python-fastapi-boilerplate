from middlewares.exception import ValidationException
from models.dtos.plateDto import CreatePlateDto


def getPlateByIdValidation(id: str):
    if id == "0":
        raise ValidationException("Id 0 olamaz.", "GPBIV.0001")


def postPlateValidation(model: CreatePlateDto):
    if model.fullName.strip() == "":
        raise ValidationException("FullName boş olamaz.", "PPV.0001")
    if model.plateString.strip() == "":
        raise ValidationException("PlateString boş olamaz.", "PPV.0002")
