import uuid
import datetime
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class BaseTable(BaseModel):
    id = Column(uuid.UUID, default=uuid.uuid4, primary_key=True)
    cDate = Column(DateTime, default=datetime.datetime.now)
    mDate = Column(DateTime, default=datetime.datetime.now)
    isDelete = Column(bool, default=False)
    isActive = Column(bool, default=True)


class User(Base, BaseTable):
    __tablename__ = 'users'

    hashedPassword = Column(str, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    identityNumber = Column(String(min=10, max=11),
                            unique=True, nullable=False)
    fullName = Column(String(min=3, max=256), nullable=False)
    phoneNumber = Column(String(20), nullable=True)
    birthday = Column(DateTime, nullable=True)


class Address(BaseTable, table=True):
    __tablename__ = 'addresses'

    title = Column(String(50), nullable=False)
    description = Column(String(256), nullable=False)

    userId = Column(uuid.UUID, ForeignKey('users.id'))
    user = relationship('User', back_populates='addresses')
