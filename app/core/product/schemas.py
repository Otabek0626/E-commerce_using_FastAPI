from pydantic import BaseModel, EmailStr, conint
from typing import Optional, List

class ProductCategoryCreate(BaseModel):
    name: str
    description: str

class ProductCategoryReturn(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: str
    category_id: int

class ProductReturn(BaseModel):
    id: int
    name: str
    description: str
    category_id: int

    class Config:
        orm_mode = True
