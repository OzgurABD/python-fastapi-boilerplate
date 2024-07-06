from pydantic import BaseModel
from models.dtos.userDto import UserDto


class UserRequestModel(BaseModel):
    email: str | None = None
    identityNumber: str | None = None
    phoneNumber: str | None = None
    birthday: str | None = None
    name: str | None = None
    surName: str | None = None
    password: str | None = None

    def MapToUserDto(model) -> UserDto:
        return UserDto(
            hashedPassword=model.password,
            fullName=f"{model.name} {model.surName}",
            email=model.email,
            identityNumber=model.identityNumber,
            phoneNumber=model.phoneNumber,
            birthday=model.birthday
        )
