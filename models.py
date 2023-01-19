from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base
 
class Usuario(Base): 
    __tablename__ = "users"
 
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)    
    name = Column(String)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String)
    phones = Column(String)
    created = Column(DateTime(timezone=False))
    modified = Column(DateTime(timezone=False))
    last_login = Column(DateTime(timezone=False))
    is_active = Column(Boolean, server_default='True')
    token = Column(String)
