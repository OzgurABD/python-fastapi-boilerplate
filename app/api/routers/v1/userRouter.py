import uuid
from fastapi import APIRouter
from business.userBusiness import UserBusiness
from models.requests.userRegisterRequestModel import UserRegisterRequestModel
from models.responses.userResponseModel import UserResponseModel, UsersResponseModel
from models.commonModel import Login, Token
from core.authorization import authorize
from api.deps import CurrentUserDep

router = APIRouter()

# async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

# @router.get("/check")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons


@router.post("/login", response_model=Token)
async def login(model: Login) -> Token:
    return UserBusiness.login(model)


@router.post("/register", response_model=UserResponseModel)
async def register(model: UserRegisterRequestModel) -> UserResponseModel:
    # TODO MapToRegisterDtoExt alternatives to MapToRegisterDto, The method (MapToRegisterDto) is located in the class it depends on.
    # return UserBusiness.register(model.MapToRegisterDtoExt())
    return UserBusiness.register(model.MapToRegisterDto())


@router.get("/{id}", response_model=UserResponseModel)
@authorize(role="admin")
async def getById(id: uuid.UUID, currentUser: CurrentUserDep) -> UserResponseModel:
    return UserBusiness.getById(id)


@router.get("/getAll", response_model=UsersResponseModel)
@authorize(role="superAdmin")
async def getAll(currentUser: CurrentUserDep) -> UsersResponseModel:
    return UserBusiness.getAll()
