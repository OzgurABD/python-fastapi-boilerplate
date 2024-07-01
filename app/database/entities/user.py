import uuid
import datetime
from sqlalchemy import Column, ForeignKey, String, SmallInteger, DateTime, Uuid
from sqlalchemy.orm import relationship
from dbSession import Base


class BaseTable:
    id = Column(Uuid, primary_key=True, default=lambda: str(uuid.uuid4()))
    cDate = Column(DateTime, default=datetime.datetime.now)
    mDate = Column(DateTime, default=datetime.datetime.now)
    status = Column(SmallInteger, default=True)


class User(Base, BaseTable):
    __tablename__ = 'users'

    hashedPassword = Column(String, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    identityNumber = Column(String(11), unique=True, nullable=False)
    fullName = Column(String(256), nullable=False)
    phoneNumber = Column(String(20), nullable=True)
    birthday = Column(DateTime, nullable=True)


class Address(Base, BaseTable):
    __tablename__ = 'addresses'

    title = Column(String(50), nullable=False)
    description = Column(String(256), nullable=False)

    userId = Column(Uuid, ForeignKey('users.id'))
    user = relationship('User', back_populates='addresses')
