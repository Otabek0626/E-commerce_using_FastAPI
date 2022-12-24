from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from ..database import Base

class Shopping(Base):
    __tablename__ = "shoppings"

    id = Column(Integer, primary_key = True, nullable = False)
    
    

    created_at = Column(TIMESTAMP(timezone=False), nullable=False, server_default=text('now()'))
    phone_number = Column(String, nullable=True, unique=True)