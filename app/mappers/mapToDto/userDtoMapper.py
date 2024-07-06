from database.entities.user import User
from models.dtos.userDto import UserDto, UserLoginDto
from models.requests.userRequestModel import UserRequestModel


@staticmethod
def MapToUserDto(model: UserRequestModel) -> UserDto:
    return UserDto(
        fullName=f"{model.name} {model.surName}",
        email=model.email,
        identityNumber=model.identityNumber,
        phoneNumber=model.phoneNumber,
        birthday=model.birthday
    )


@staticmethod
def MapUserEntityToUserLoginDto(model: User) -> UserLoginDto:
    return UserLoginDto(
        id=model.id,
        email=model.email,
        identityNumber=model.identityNumber,
        hashedPassword=model.hashedPassword
    )


@staticmethod
def MapUserEntityToUserDto(model: User) -> UserDto:
    return UserDto(
        id=model.id,
        email=model.email,
        identityNumber=model.identityNumber,
        fullName=model.fullName,
        phoneNumber=model.phoneNumber,
        birthday=model.birthday
    )


@staticmethod
def MapUsersEntityToUsersDto(model: list[User]) -> list[UserDto]:
    return list(map(MapUserEntityToUserDto, model))
