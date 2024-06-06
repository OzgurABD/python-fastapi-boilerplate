"""Business Module"""

from dependency_injector.wiring import Provide, inject
from ..services import plateService, photoService
from ..services.serviceContainers import Application


@inject
def getPlateById(
    id: str,
    plate_service: plateService.PlateService = Provide[Application.services.plate],
) -> None:
    return plate_service.getById(id)


@inject
def postPlatePhoto(
    plateString: str,
    photo: str,
    plate_service: plateService.PlateService = Provide[Application.services.plate],
    photo_service: photoService.PlatePhotoService = Provide[Application.services.photo],
) -> None:
    plate = plate_service.getByString(plateString)
    result = photo_service.postPhoto(plate, photo)
    return result
