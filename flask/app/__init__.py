from flask import Flask
from os import environ
from .config import *

app = Flask(__name__)

environment = environ.get('FLASK_ENV', default='development')
if environment == 'development':
    cfg = config.DevelopmentConfig()
elif environment == 'production':
    cfg = config.ProductionConfig()
else:
    import sys
    sys.exit(-1)

app.config.from_object(cfg)

from app import views
