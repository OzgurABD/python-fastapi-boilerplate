"""Endpoints module."""

import uuid
from fastapi import APIRouter, Query
from constants import ADMIN, SUPER_ADMIN
from core.authorization import authorize
from dependencies import DbSessionDep, CurrentUserDep
from containers import userBusiness as _userBusiness
from models.requests.userRequestModel import UserRequestModel
from models.responses.userResponseModel import UserResponseModel, UsersResponseModel
from models.commonModel import Login, Token
from models.dtos.userDto import UserDto
from mappers.mapToModel.userModelMapper import MapToUserModel, MapToUsersModel

router = APIRouter()


@router.post("/login", response_model=Token)
async def login(model: Login, db=DbSessionDep) -> Token:
    return _userBusiness.login(model, db)


@router.post("/register", response_model=UserResponseModel)
async def register(model: UserRequestModel, db=DbSessionDep) -> UserResponseModel:
    result: UserDto = _userBusiness.register(model.MapToUserDto(), db)
    return MapToUserModel(result)


@router.get("/{id}", response_model=UserResponseModel)
@authorize(role=ADMIN)
async def getById(id: uuid.UUID, currentUser=CurrentUserDep, db=DbSessionDep) -> UserResponseModel:
    result: UserDto = _userBusiness.getById(id, db)
    return MapToUserModel(result)


@router.put("/{id}", response_model=UserResponseModel)
@authorize(role=ADMIN)
async def update(id: uuid.UUID, model: UserRequestModel, currentUser=CurrentUserDep, db=DbSessionDep) -> UserResponseModel:
    result: UserDto = _userBusiness.update(id, model, db)
    return MapToUserModel(result)


@router.delete("/{id}", response_model=bool)
@authorize(role=ADMIN)
async def softDelete(id: uuid.UUID, currentUser=CurrentUserDep, db=DbSessionDep) -> bool:
    result: bool = _userBusiness.softDelete(id, db)
    return result


@router.delete("/{id}", response_model=bool)
@authorize(role=SUPER_ADMIN)
async def hardDelete(id: uuid.UUID, currentUser=CurrentUserDep, db=DbSessionDep) -> bool:
    result: bool = _userBusiness.hardDelete(id, db)
    return result


@router.get("/getAll/", response_model=UsersResponseModel)
@authorize(role=SUPER_ADMIN)
async def getAll(q: list[str] | None = Query(default=None), currentUser=CurrentUserDep, db=DbSessionDep) -> UsersResponseModel:
    result: list[UserDto] = _userBusiness.getAll(q, db)
    return MapToUsersModel(result)
