from .models import Notif
from rest_framework import serializers

class NotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notif
        fields = '__all__'