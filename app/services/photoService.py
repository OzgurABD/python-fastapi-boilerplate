"""Services module."""

import sqlite3
from typing import Dict
from mypy_boto3_s3 import S3Client
from .baseService import BaseService


class PlatePhotoService(BaseService):

    def __init__(self, db: sqlite3.Connection, s3: S3Client) -> None:
        self.db = db
        self.s3 = s3
        super().__init__()

    def postPhoto(self, plate: Dict[str, str], photo_path: str) -> None:
        self.logger.debug(
            "Photo %s has been successfully uploaded by plate %s",
            photo_path,
            plate["pNum"],
        )
