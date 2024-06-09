"""Business Module"""

# from dependency_injector.wiring import Provide, inject
from business.iPlateBusiness import IPlateBusiness
from services.plateService import PlateService
from business.plateBusinessValidation import PlateBusinessValidation
from models.serviceResult import ServiceResult
from models.responses.plateResponseModel import PlateResponseModel


# from ..services.serviceContainers import Application


class PlateBusiness(IPlateBusiness):

    # @inject
    def getPlateById(
        id: str,
        # plate_service: plateService.PlateService = Provide[Application.services.plate],
    ) -> PlateResponseModel:
        PlateBusinessValidation.getPlateByIdValidation(id)
        result: ServiceResult = PlateService.getById(id)
        return PlateResponseModel(id=id, plateString=result.data)


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
