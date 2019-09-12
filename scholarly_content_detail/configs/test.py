from scholarly_content_detail.configs.base import *

# Flask
DEBUG = True
TESTING = True
CSRF_ENABLED = True
SECRET_KEY = 'secret key'

# SQL Alchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
SQLALCHEMY_TRACK_MODIFICATIONS = True