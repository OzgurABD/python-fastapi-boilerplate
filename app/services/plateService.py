"""Services module."""

import sqlite3
from models.serviceResult import ServiceResult

# from .baseService import BaseService
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
