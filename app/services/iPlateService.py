"""Interface class module."""

from abc import ABC, abstractmethod
from models.serviceResult import ServiceResult


class IPlateService(ABC):

    @abstractmethod
    def getById(self, id: str) -> ServiceResult[str]:
        pass

    @abstractmethod
    def getByString(self, plateString: str) -> ServiceResult[str]:
        pass
