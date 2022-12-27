from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from datetime import datetime

from ..database import Base

from ..auth.models import User


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)

#     username = Column(String, nullable = False, unique = True)
#     email = Column(String, nullable = False, unique = True)
#     password = Column(String, nullable = False)
#     first_name = Column(String)
#     last_name = Column(String)
#     phone_number = Column(String, nullable=True, unique=True)
    
#     payments = relationship("Payment", back_populates="owner")
#     addresses = relationship("Address", back_populates="owner")

#     created_at = Column(DateTime, nullable=False, default=datetime.now())
#     updated_at = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())


class Address(Base):
    __tablename__ = "user_addresses"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable = False)
    receiver_name = Column(String, nullable = False)
    receiver_mobile = Column(String, nullable = False)
    full_address = Column(String, nullable = False)

    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())


class Payment(Base):
    __tablename__ = "user_payments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    payment_type = Column(String, nullable = False)
    provider = Column(String, nullable = False)
    holder_name = Column(String, nullable = False)
    account_number = Column(Integer, nullable = False)
    cvc_number = Column(Integer, nullable = False)
    expire_date = Column(String, nullable = False)

    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
