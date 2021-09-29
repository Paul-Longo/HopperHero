from rest_framework import serializers
from .models import Wod

class WodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wod
        fields = ['id', 'name', 'description']
