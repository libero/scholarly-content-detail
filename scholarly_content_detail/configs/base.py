"""
Base config file to provide global settings that should be overwritten with
environment specific values.
"""

# Flask
DEBUG = False
TESTING = False
CSRF_ENABLED = True
SECRET_KEY = ''

# SQL Alchemy
SQLALCHEMY_DATABASE_URI = ''
SQLALCHEMY_TRACK_MODIFICATIONS = False
