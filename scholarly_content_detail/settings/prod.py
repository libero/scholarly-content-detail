"""
Add/override production specific settings here
"""
import os

from .base import *


DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {}
