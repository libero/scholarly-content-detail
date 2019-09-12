import os

from scholarly_content_detail.configs.base import *


# Flask
DEBUG = True
SECRET_KEY = 'secret key'

# SQL Alchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@db:5432/{}'.format(
    os.getenv('POSTGRES_USER'),
    os.getenv('POSTGRES_PASSWORD'),
    os.getenv('POSTGRES_DB')
)
