from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from datetime import datetime

from ..database import Base


class Product_Category(Base):
    __tablename__ = "product_categories"

    id = Column(Integer, primary_key = True, nullable = False)
    
    name = Column(String, nullable = False)
    description = Column(String, nullable = False)

    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key = True, nullable = False)
    
    name = Column(String, nullable = False)
    description = Column(String, nullable = False)
    category_id = Column(Integer, ForeignKey("product_categories.id"), server_default="1")

    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())