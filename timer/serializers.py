from rest_framework import serializers
from timer.models import Timer


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = '__all__'
