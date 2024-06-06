"""Interface class module."""

from abc import ABC, abstractmethod


class IPlateService(ABC):

    @abstractmethod
    def getById(self, id: str) -> dict:
        pass

    @abstractmethod
    def getByString(self, plateString: str) -> dict:
        pass
