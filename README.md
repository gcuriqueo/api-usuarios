- Levantar contenedor con base de datos postgres:
```
docker-compose up -d
```
- Levantar API:
```
uvicorn main:app --host localhost --port 8000 --reload
```