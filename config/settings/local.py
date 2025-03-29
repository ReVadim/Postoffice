from .base import *

DEBUG = True

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'post_db.sqlite3',
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
