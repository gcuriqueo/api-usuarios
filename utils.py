from jwt import encode
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
import re

SECRET_KEY = 'deff1952d59f883ece260e8683fed21ab0ad9a53323eca4f'

def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date

def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2) }, key=SECRET_KEY, algorithm="HS256")
    return token

def validate_pass(passwd):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d{2,})(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{7,20}$"
    pat = re.compile(reg)             
    mat = re.search(pat, passwd)
    return mat

