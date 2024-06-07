"""Interface class module."""

from abc import ABC, abstractmethod
from models.responses.plateResponseModel import PlateResponseModel


class IPlateBusiness(ABC):

    @abstractmethod
    def getPlateById(self, id: str) -> PlateResponseModel:
        pass
