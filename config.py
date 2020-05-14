import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or "la llave secreta de jerry...el amor"