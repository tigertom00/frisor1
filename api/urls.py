from django.contrib import admin
from django.urls import path, include

# from api.settings.base import BASE_DIR
# from api.settings.dev import VENV_PATH
# import sys
# print(BASE_DIR, file=sys.stderr)
# print(VENV_PATH, file=sys.stderr)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('timer.urls')),
    path('', include('users.urls')),
]
