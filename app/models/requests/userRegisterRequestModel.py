from pydantic import BaseModel
from dtos.userDto import UserRegisterDto


class UserRegisterRequestModel(BaseModel):
    email: str
    identityNumber: str
    phoneNumber: str | None = None
    name: str
    surName: str

    def MapToRegisterDto(model) -> UserRegisterDto:
        return UserRegisterDto(
            fullName=f"{model.name} {model.surName}",
            email=model.email,
            phoneNumber=model.phoneNumber,
        )
