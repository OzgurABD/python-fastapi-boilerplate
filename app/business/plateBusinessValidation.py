from middlewares.exception import ValidationException


class PlateBusinessValidation:
    def getPlateByIdValidation(id: str):
        if id == "0":
            raise ValidationException("Id 0 olamaz.", "GPBIV.0001")
