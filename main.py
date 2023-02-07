from fastapi import FastAPI,status,Depends,Depends, HTTPException

import models, schemas, crud, utils, json
from database import SessionLocal, engine

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError

from sqlalchemy.orm import Session
import uvicorn
from email_validator import validate_email, EmailNotValidError

models.Base.metadata.create_all(bind=engine) #Crea base de datos

app = FastAPI(title="API USUARIOS")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/crear_usuario/")
def crear_usuario(usuario: schemas.UsuarioBase, db: Session = Depends(get_db)):
    try:
        validate_email(usuario.email, check_deliverability=False)
        flag = utils.validate_pass(usuario.password)
        if flag: 
            db_user = crud.get_user_by_email(db, email=usuario.email)
            if db_user:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                    detail='El correo ya se encuentra registrado')   

            user_save = crud.create_user(db=db, user=usuario)
            user_save.phones = json.loads(user_save.phones)
            json_user_data = jsonable_encoder(user_save)

            return JSONResponse(content=json_user_data, status_code=status.HTTP_201_CREATED)
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail='La contraseña no cumple con los requisitos. Debe tener entre 7 y 20 caracteres, una mayúscula, letras minúsculas, dos números, y un caracter especial.')   
    except EmailNotValidError as e:
        print(e)
        raise HTTPException(detail=f"'{usuario.email}' no es un correo válido",
                            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)    


#Descomentar si desea debuguear el código
#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)