from typing import Optional
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import bcrypt
from models.commonModel import TokenPayload

SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verifyPassword(plainPassword: str, hashedPassword: str) -> bool:
    return bcrypt.checkpw(plainPassword.encode('utf-8'), hashedPassword.encode("utf-8"))


def hashPassword(password: str) -> str:
    return str(bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()), encoding='utf-8')


def createToken(
    data: dict,
    expires_delta: Optional[timedelta] = timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
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
        role: str = payload.get("role")
        if userId is None:
            return None
    except JWTError:
        return None
    return TokenPayload(userId=userId, userName=userName, role=role)
