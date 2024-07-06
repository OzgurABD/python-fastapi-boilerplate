"""Containers module."""

from business.userBusiness import UserBusiness
from business.iUserBusiness import IUserBusiness


class ContainerFactory:
    @staticmethod
    def userBusinessContainer() -> IUserBusiness: return UserBusiness


userBusiness = ContainerFactory.userBusinessContainer()
