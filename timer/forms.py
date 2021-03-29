from django import forms
from .models import Timer


class TimerForm(forms.ModelForm):
    class Meta:
        model = Timer
        fields = '__all__'
