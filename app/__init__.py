from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

from app import rutas

if __name__ == '__main__':
    app.run()
