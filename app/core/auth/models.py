from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime

from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, nullable = False, unique = True)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    role = Column(String, nullable = False, server_default="customer", default="customer")

    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())