from pydantic import BaseModel, EmailStr, conint
from typing import Optional
from datetime import datetime, timedelta

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class TokenExpire(BaseModel):
    username: Optional[str] = None
    expires: datetime