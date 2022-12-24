from pydantic import BaseModel, EmailStr, conint
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: str


class UserReturn(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        orm_mode = True

class AddressCreate(BaseModel):
    title: str
    receiver_name: str
    receiver_mobile: str
    full_address: str

class AddressReturn(BaseModel):
    id: int
    title: str
    receiver_name: str
    receiver_mobile: str
    full_address: str

    class Config:
        orm_mode = True
