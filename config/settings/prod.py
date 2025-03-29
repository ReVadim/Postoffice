import os
from .base import *

DEBUG = False

ADMINS = [
    ('Re_Vadim', 'revani@yandex.ru'),
]

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1').split(' ')  # in .env DJANGO_ALLOWED_HOSTS = 127.0.0.1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}
STATIC_ROOT = BASE_DIR / 'static'
