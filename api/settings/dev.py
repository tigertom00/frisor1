from .base import *

DEBUG = True

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar',
    'testing',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# * Paths
VENV_PATH = Path(BASE_DIR).joinpath('local_static_files')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [Path(BASE_DIR) / 'static_in_env']
STATIC_ROOT = Path(VENV_PATH) / 'static_root'
MEDIA_ROOT = Path(VENV_PATH) / 'media_root'

# * Databae
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(BASE_DIR) / 'db.sqlite3',
    }
}

# * Email
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = Path(VENV_PATH) / 'email'

# * Cors Headers
CORS_ALLOWED_ORIGINS = [
    "https://nxfs.no",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:5500"
]

# * Debug Toolbar
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}
