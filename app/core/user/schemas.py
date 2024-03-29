from pydantic import BaseModel, EmailStr, conint
from typing import Optional, List

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

class PaymentCreate(BaseModel):
    payment_type: str
    provider: str
    holder_name: str
    account_number: int
    cvc_number: int
    expire_date: str

class PaymentReturn(BaseModel):
    id: int
    payment_type: str
    provider: str
    holder_name: str
    account_number: int
    cvc_number: int
    expire_date: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserReturn(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


