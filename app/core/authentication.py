from typing import Optional
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

passwordContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verifyPassword(plainPassword, hashedPassword):
    return passwordContext.verify(plainPassword, hashedPassword)


def hashPassword(password):
    return passwordContext.hash(password)


def createToken(
    data: dict,
    expires_delta: Optional[timedelta] = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
):
    _claims = data.copy()
    expire = datetime.now() + expires_delta

    _claims.update({"exp": expire})
    _jwt = jwt.encode(_claims, SECRET_KEY, algorithm=ALGORITHM)
    return _jwt


async def contextUser(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        userId: str = payload.get("userId")
        userName: str = payload.get("userName")
        roles: list = payload.get("roles")
        if userId is None:
            return None
    except JWTError:
        return None
    return {"userId": userId, "userName": userName, "roles": roles}
