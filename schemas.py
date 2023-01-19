from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List
import uuid

class UsuarioBase(BaseModel):
    name: str
    email: str
    password: str
    phones: str
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