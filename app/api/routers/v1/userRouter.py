"""Endpoints module."""

import uuid
from fastapi import APIRouter
from dependency_injector.wiring import inject
from models.requests.userRegisterRequestModel import UserRegisterRequestModel
from models.responses.userResponseModel import UserResponseModel, UsersResponseModel
from models.commonModel import Login, Token
from core.authorization import authorize
from api.deps import CurrentUserDep, UserServiceDep

router = APIRouter()

# async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

# @router.get("/check")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons


@router.post("/login", response_model=Token)
@inject
async def login(model: Login) -> Token:
    return UserServiceDep.login(model)


@router.post("/register", response_model=UserResponseModel)
@inject
async def register(model: UserRegisterRequestModel) -> UserResponseModel:
    # TODO MapToRegisterDtoExt alternatives to MapToRegisterDto, The method (MapToRegisterDto) is located in the class it depends on.
    # return UserServiceDep.register(model.MapToRegisterDtoExt())
    return UserServiceDep.register(model.MapToRegisterDto())


@router.get("/{id}", response_model=UserResponseModel)
@authorize(role="admin")
@inject
async def getById(id: uuid.UUID, currentUser: CurrentUserDep) -> UserResponseModel:
    return UserServiceDep.getById(id)


@router.get("/getAll", response_model=UsersResponseModel)
@authorize(role="superAdmin")
@inject
async def getAll(currentUser: CurrentUserDep) -> UsersResponseModel:
    return UserServiceDep.getAll()
