"""Endpoints module."""

import uuid
from fastapi import APIRouter, Query
from constants import ADMIN, SUPER_ADMIN
from core.authorization import authorize
from dependencies import DbSessionDep, CurrentUserDep, CommonParamsDep
from containers import userBusiness as _userBusiness
from models.requests.userRequestModel import UserRequestModel
from models.responses.userResponseModel import UserResponseModel, UsersResponseModel
from models.commonModel import Login, Token, PaginationQuery, ResponseModel, ResponsePaginationModel
from models.dtos.userDto import UserDto
from mappers.mapToModel.userModelMapper import MapToUserModel, MapToUsersModel

router = APIRouter()


@router.post("/login", response_model=ResponseModel[Token])
async def login(model: Login, db=DbSessionDep) -> ResponseModel[Token]:
    return _userBusiness.login(model, db)


@router.post("/register", response_model=UserResponseModel)
async def register(model: UserRequestModel, db=DbSessionDep) -> UserResponseModel:
    result: ResponseModel[UserDto] = _userBusiness.register(
        model.MapToUserDto(), db)
    return MapToUserModel(result.data)


@router.get("/{id}", response_model=UserResponseModel)
@authorize(role=ADMIN)
async def getById(id: uuid.UUID, currentUser=CurrentUserDep, db=DbSessionDep) -> UserResponseModel:
    result: ResponseModel[UserDto] = _userBusiness.getById(id, db)
    return MapToUserModel(result.data)


@router.put("/{id}", response_model=UserResponseModel)
@authorize(role=ADMIN)
async def update(id: uuid.UUID, model: UserRequestModel, currentUser=CurrentUserDep, db=DbSessionDep) -> UserResponseModel:
    result: ResponseModel[UserDto] = _userBusiness.update(id, model, db)
    return MapToUserModel(result.data)


@router.delete("/{id}", response_model=ResponseModel[bool])
@authorize(role=ADMIN)
async def softDelete(id: uuid.UUID, currentUser=CurrentUserDep, db=DbSessionDep) -> bool:
    return _userBusiness.softDelete(id, db)


@router.delete("/{id}", response_model=ResponseModel[bool])
@authorize(role=SUPER_ADMIN)
async def hardDelete(id: uuid.UUID, currentUser=CurrentUserDep, db=DbSessionDep) -> bool:
    return _userBusiness.hardDelete(id, db)


@router.get("/getAll/", response_model=UsersResponseModel)
@authorize(role=SUPER_ADMIN)
async def getAll(email: str | None = None, params=CommonParamsDep, currentUser=CurrentUserDep, db=DbSessionDep) -> UsersResponseModel:
    result: ResponsePaginationModel[list[UserDto]] = _userBusiness.getAll({**params, **{"email": email}}, db) #fmt:off 
    return MapToUsersModel(result) #fmt:on
