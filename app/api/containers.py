"""Containers module."""

from dependency_injector import containers, providers
from database.dbSession import Database
from core.config import settings
from services.userService import UserService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=["api.routers.v1.userRouter"], auto_wire=False)
    # config = providers.Configuration(yaml_files=["config.yml"])
    db = providers.Singleton(
        Database, db_url=settings.SQLALCHEMY_DATABASE_URI)  # config.db.url

    userService = providers.Factory(UserService)
