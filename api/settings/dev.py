from .base import *

SECRET_KEY = ')8#izff-tz7t*o_du)+jb7)1y3i_0v2-l-oci&uij6#ll+n6t_'
DEBUG = True
VENV_PATH = Path(BASE_DIR).joinpath('local_static_files')

ALLOWED_HOSTS = []

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [Path(BASE_DIR) / 'static_in_env']
STATIC_ROOT = Path(VENV_PATH) / 'static_root'
MEDIA_ROOT = Path(VENV_PATH) / 'media_root'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(BASE_DIR) / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = Path(VENV_PATH) / 'email'
