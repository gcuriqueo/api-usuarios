from sqlalchemy.orm import Session
from jose import JWTError, jwt
import models, schemas, utils, json
from datetime import datetime

def get_user_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def create_user(db: Session, user: schemas.UsuarioResponse):
    dict_user = dict(zip(['name','password'], [user.name, user.password]))
    token_user = utils.write_token(dict_user)
    jsonPhoneStr = json.dumps([obj.__dict__ for obj in user.phones])
    
    db_user = models.Usuario(
        name = user.name,
        email = user.email, 
        password = user.password,
        phones = jsonPhoneStr,
        created = datetime.now() ,
        modified = datetime.now(),
        last_login = datetime.now(),        
        token = token_user )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
