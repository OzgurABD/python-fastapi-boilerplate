import uuid
import datetime
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel


class BaseTable(SQLModel):
    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    isDelete: bool = False
    isActive: bool = True
    cDate: datetime = datetime.datetime.now()
    mDate: datetime = datetime.datetime.now()


class User(BaseTable, table=True):
    hashedPassword: str
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    identityNumber: str = Field(min_length=10, max_length=11)
    fullName: str | None = Field(default=None, max_length=255)
    phoneNumber: str | None = Field(default=None, max_length=20)
    birthday: datetime.time | None = None
    addresses: list["Address"] = Relationship(back_populates="user")


class Address(BaseTable, table=True):
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(min_length=1, max_length=255)
    userId: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    user: User | None = Relationship(back_populates="addresses")
