"""Services module."""

import sqlite3
from typing import Dict

# from .baseService import BaseService
from .iPlateService import IPlateService


class PlateService(IPlateService):

    def __init__(self, db: sqlite3.Connection) -> None:
        self.db = db
        super().__init__()

    def getById(self, id: str) -> Dict[str, str]:
        self.logger.debug("Plate %s has been found in database", id)
        return {"id": id, "result": "..."}

    def getByString(self, plateString: str) -> Dict[str, str]:
        self.logger.debug("Plate %s has been found in database", plateString)
        return {"plateString": plateString, "result": "..."}
