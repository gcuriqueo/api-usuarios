from sqlalchemy.orm import Session
from jose import JWTError, jwt
import models, schemas, utils
from datetime import datetime

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

def get_user_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def create_user(db: Session, user: schemas.UsuarioResponse):
    dict_user = dict(zip(['name','password'], [user.name, user.password]))
    token_user = utils.write_token(dict_user)
    
    db_user = models.Usuario(
        name = user.name,
        email = user.email, 
        password = user.password,
        phones = user.phones,
        created = datetime.now() ,
        modified = datetime.now(),
        last_login = datetime.now(),        
        token = token_user )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
