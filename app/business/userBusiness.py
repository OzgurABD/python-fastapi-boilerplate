"""Business Module"""

# from dependency_injector.wiring import Provide, inject
from middlewares.exception import BusinessException
from core.authentication import createToken, hashPassword
from business.iUserBusiness import IUserBusiness
from business.userBusinessValidation import *
from services.userService import UserService
from models.serviceResult import ServiceResult
from models.responses.userResponseModel import UserResponseModel, UsersResponseModel
from models.dtos.userDto import UserDto, UserRegisterDto
from models.commonModel import Token

# from ..services.serviceContainers import Application

@IUserBusiness.register
class UserBusiness(IUserBusiness):

    def login(model: Login) -> Token:
        loginValidation(model)
        try:
            hashedPassword = hashPassword(model.password)
            result: ServiceResult[UserDto] = UserService.login(
                model.userName, hashedPassword
            )

            if result.success != True:
                raise ValidationException(
                    "Incorrect Username Or Password", "UBL.0001")
            else:
                token = createToken(
                    data={
                        "userId": result.data.id,
                        "userName": result.data.email,
                        "roles": ["admin"],
                    }
                )
                return Token(token)
        except:
            raise BusinessException("Error Login Business", "UBL.0002")

    def getById(id: uuid.UUID) -> UserResponseModel:
        getByIdValidation(id)
        try:
            result: ServiceResult[UserDto] = UserService.getById(id)
            if result.success != True:
                raise ValidationException("Not Found User", "UBL.0003")

            return UserResponseModel(data=result.data)
        except:
            raise BusinessException("Error GetById Business", "UBGBI.0004")

    def getAll() -> UsersResponseModel:
        try:
            result: ServiceResult[list[UserDto]] = UserService.getAll()
            return UsersResponseModel(data=result.data)
        except:
            raise BusinessException("Error GetAll Business", "UBGBI.0005")

    def register(model: UserRegisterDto) -> UserResponseModel:
        pass


# @inject
# def postPlatePhoto(
#     plateString: str,
#     photo: str,
#     plate_service: plateService.PlateService = Provide[Application.services.plate],
#     photo_service: photoService.PlatePhotoService = Provide[Application.services.photo],
# ) -> None:
#     plate = plate_service.getByString(plateString)
#     result = photo_service.postPhoto(plate, photo)
#     return result
