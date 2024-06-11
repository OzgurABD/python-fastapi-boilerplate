from pydantic import BaseModel
from models.dtos.plateDto import CreatePlateDto


class InsertPlateRequestModel(BaseModel):
    plateString: str
    name: str
    surName: str

    def MapToCreateDto(model) -> CreatePlateDto:
        return CreatePlateDto(
            plateString=model.plateString,
            fullName=f"{model.name} {model.surName}",
        )
