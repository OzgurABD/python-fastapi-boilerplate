from models.dtos.userDto import UserDto
from models.responses.userResponseModel import UserModel, UserResponseModel, UsersResponseModel


def MapUserDtoToUserModel(model: UserDto) -> UserModel:
    return UserModel(id=model.id, email=model.email, fullName=model.fullName, phoneNumber=model.phoneNumber)


def MapToUserModel(model: UserDto) -> UserResponseModel:
    return UserResponseModel(data=MapUserDtoToUserModel(model))


def MapToUsersModel(model: list[UserDto]) -> UsersResponseModel:
    return UsersResponseModel(data=list(map(MapUserDtoToUserModel, model)))
