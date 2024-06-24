"""Services module."""

import sqlite3
from models.dtos.plateDto import CreatePlateDto, PlateDto
from models.serviceResult import ServiceResult
from .iPlateService import IPlateService


class PlateService(IPlateService):

    def __init__(self, db: sqlite3.Connection) -> None:
        self.db = db
        super().__init__()

    def getById(id: str) -> ServiceResult[str]:
        # self.logger.debug("Plate %s has been found in database", id)
        return ServiceResult[str](data=id, success=True)

    def getByString(plateString: str) -> ServiceResult[str]:
        # self.logger.debug("Plate %s has been found in database", plateString)
        return ServiceResult[str](data=plateString, success=True)

    def postPlate(model: CreatePlateDto) -> ServiceResult[PlateDto]:
        # self.logger.debug("Plate %s has been found in database", plateString)
        result = PlateDto(
            id=f"34-xx-{model.fullName}",
            plateString=model.plateString,
            fullName=model.fullName,
        )
        return ServiceResult[PlateDto](data=result, success=True)
