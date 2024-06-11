"""Business Module"""

# from dependency_injector.wiring import Provide, inject
from middlewares.exception import BusinessException
from business.iPlateBusiness import IPlateBusiness
from business.plateBusinessValidation import *
from services.plateService import PlateService
from models.serviceResult import ServiceResult
from models.responses.plateResponseModel import PlateResponseModel
from models.dtos.plateDto import CreatePlateDto, PlateDto

# from ..services.serviceContainers import Application


class PlateBusiness(IPlateBusiness):

    # @inject
    def getPlateById(
        id: str,
        # plate_service: plateService.PlateService = Provide[Application.services.plate],
    ) -> PlateResponseModel:
        getPlateByIdValidation(id)
        try:
            result: ServiceResult[str] = PlateService.getById(id)
            return PlateResponseModel(id=id, plateString=result.data)
        except:
            raise BusinessException("Error getPlateById", "PBGP.0001")

    def postPlate(model: CreatePlateDto) -> PlateResponseModel:
        postPlateValidation(model)
        try:
            result: ServiceResult[PlateDto] = PlateService.postPlate(model)
            return PlateResponseModel(
                id=result.data.id,
                plateString=result.data.plateString,
                fullName=result.data.fullName,
            )
        except:
            raise BusinessException("Error postPlate", "PBPP.0001")


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
