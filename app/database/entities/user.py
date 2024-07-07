import uuid
import datetime
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, SmallInteger, DateTime, Uuid, Boolean
from ..session import Base

# fmt: off

class BaseTable:
    id: Mapped[Uuid] = mapped_column(Uuid, primary_key=True, default=lambda: str(uuid.uuid4()))
    cDate: Mapped[DateTime] = mapped_column(DateTime, default=datetime.datetime.now())
    mDate: Mapped[DateTime] = mapped_column(DateTime, default=None, nullable=True)
    status: Mapped[SmallInteger] = mapped_column(SmallInteger, default=None, nullable=True)
    isDelete: Mapped[Boolean] = mapped_column(Boolean, default=False)


class User(Base, BaseTable):
    __tablename__ = 'users'

    hashedPassword: Mapped[String] = mapped_column(String, nullable=False)
    email: Mapped[String] = mapped_column(String(100), unique=True, nullable=False)
    identityNumber: Mapped[String] = mapped_column(String(11), unique=True, nullable=False)
    fullName: Mapped[String] = mapped_column(String(256), nullable=False)
    phoneNumber: Mapped[String] = mapped_column(String(10), nullable=True)
    birthday: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    addresses: Mapped[Optional[List["Address"]]] = relationship()


class Address(Base, BaseTable):
    __tablename__ = 'addresses'

    title: Mapped[String] = mapped_column(String(50), nullable=False)
    description: Mapped[String] = mapped_column(String(256), nullable=False)

    userId: Mapped[Uuid] = mapped_column(ForeignKey("users.id"))
