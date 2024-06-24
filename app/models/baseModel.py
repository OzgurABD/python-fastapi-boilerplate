from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel


class Message(SQLModel):
    message: str


class Token(SQLModel):
    token: str
    tokenType: str = "bearer"


class TokenPayload(SQLModel):
    userId: str | None = None
    userName: str | None = None
    roles: list | None = None


class NewPassword(SQLModel):
    token: str
    newPassword: str


class UserLogin(BaseModel):
    userName: str
    password: str


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    isActive: bool = True
    fullName: str | None = None


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    items: list["Item"] = Relationship(back_populates="owner")
