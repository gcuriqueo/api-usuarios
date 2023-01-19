from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List
import uuid

class PhoneBase(BaseModel):
    number: int
    citycode: int
    contrycode: int

class UsuarioBase(BaseModel):
    name: str
    email: str
    password: str
    phones: List[PhoneBase] = []
    class Config:
        orm_mode = True    
        
class UsuarioResponse(UsuarioBase):
    id: uuid.UUID
    name: str
    email: str
    password: str
    phones: str
    created: datetime
    modified: datetime
    last_login: datetime
    is_active: bool
    token: str