from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from middlewares.exception import ValidationException
from models.baseModel import Token, UserLogin
from core.authentication import (
    createToken,
    hashPassword,
)
from core.authorization import authorize
from deps import CurrentUser

router = APIRouter()


@router.post("/login")
async def login(userLogin: OAuth2PasswordRequestForm = Depends()):
    user = None  # userService.login(userLogin)
    if not user:
        raise ValidationException("Incorrect username or password", "L.001")
    token = createToken(
        data={
            "userId": user["userId"],
            "userName": user["userName"],
            "roles": ["admin"],
        }
    )
    return Token(token)


@router.post("/register")
async def register(user: UserLogin):
    hashed_password = hashPassword(user.password)
    # userService.register(user,hashedPassword)
    return {"message": "User registered successfully"}


@router.get("/checkAdmin")
@authorize(role="admin")
async def checkAdmin(currentUser: CurrentUser):
    return {"message": "This endpoint is accessible to admin only"}


@router.get("/checkSuperAdmin")
@authorize(role="superAdmin")
async def checkSuperAdmin(currentUser: CurrentUser):
    return {"message": "This endpoint is accessible to superadmin only"}
