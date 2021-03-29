from django.contrib import admin
from . import forms
from . import models


# class CustomTimer(admin.ModelAdmin):
#     model = models.Timer
#     add_form = TimerCreationForm
#     form = TimerChangeForm
#     list_display = ['user',
#                     'dato',
#                     'text'
#                     ]
#     fieldsets = ModelAdmin.fieldsets + (
#         (None, {'fields': (
#             'user',
#             'dato',
#             'text'
#         )}),
#     )


admin.site.register(models.Timer)
