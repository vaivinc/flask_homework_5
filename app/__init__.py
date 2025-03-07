from flask import Flask
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.routes import *