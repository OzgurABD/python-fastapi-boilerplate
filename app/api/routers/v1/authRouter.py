from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from middlewares.exception import ValidationException
from models.baseModel import UserLogin
from core.authentication import (
    createToken,
    hashPassword,
    contextUser,
)
from core.authorization import authorize

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
    return {"token": token, "tokenType": "bearer"}


@router.post("/register")
async def register(user: UserLogin):
    hashed_password = hashPassword(user.password)
    # userService.register(user,hashedPassword)
    return {"message": "User registered successfully"}


@router.get("/checkAll")
@authorize(role=["admin", "superAdmin"])
async def checkAll(currentUser: dict = Depends(contextUser)):
    return {"message": "This endpoint is accessible to admin and superadmin only"}


@router.get("/checkSuperAdmin")
@authorize(role=["superAdmin"])
async def checkSuperAdmin(currentUser: dict = Depends(contextUser)):
    return {"message": "This endpoint is accessible to superadmin only"}
