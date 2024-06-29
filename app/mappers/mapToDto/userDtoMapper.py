from models.dtos.userDto import UserRegisterDto
from models.requests.userRegisterRequestModel import UserRegisterRequestModel


def MapToRegisterDto(model: UserRegisterRequestModel) -> UserRegisterDto:
    return UserRegisterDto(
        fullName=f"{model.name} {model.surName}",
        email=model.email,
        phoneNumber=model.phoneNumber,
    )


UserRegisterRequestModel.MapToRegisterDtoExt = MapToRegisterDto
