from models.dtos.plateDto import CreatePlateDto
from models.requests.insertPlateRequestModel import InsertPlateRequestModel


def MapToCreateDto(model) -> CreatePlateDto:
    return CreatePlateDto(
        plateString=model.plateString,
        fullName=f"{model.name} {model.surName}",
    )


InsertPlateRequestModel.MapToCreateDtoExt = MapToCreateDto
