"""
Add/override dev specific settings here
"""
from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'scholarly-content-detail-db',
        'USER': 'postgres',
        'PASSWORD': 'example',
        'HOST': 'db',
        'PORT': '5432'
    }
}
