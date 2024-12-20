- La actual API se desarrollo con Python 3.7 y con el framework de FastApi 0.89

- Instalar librerias necesarias para ejecutar el proyecto:
```
pip install -r requirements.txt
```

- Los datos se almacenan en una base de datos postgres, la cual se levanta con un contenedor de docker.

- El DDL de la base de datos se puede encontrar en el archivo `script.sql`, pero no es necesario ejecutarlo ya que es el propio framework de FastApi quien se encarga de crear las tablas necesarias.

- Crear un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:
  - `POSTGRES_PASSWORD`
  - `POSTGRES_USER`
  - `POSTGRES_DB`
  - `SECRET_KEY`

- Levantar contenedor con base de datos:
```
docker-compose up -d
```
- Levantar API:
```
uvicorn main:app --host localhost --port 8000 --reload
```
- Enviar los datos del usuario al endpoint `localhost:8000/crear_usuario` con el método `POST`

![img](https://raw.githubusercontent.com/gcuriqueo/api-usuarios/main/img/img.png)

