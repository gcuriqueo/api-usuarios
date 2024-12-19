from jwt import encode
from datetime import datetime, timedelta
import re, configparser
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

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

