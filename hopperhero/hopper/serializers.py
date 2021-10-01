from rest_framework import serializers
from .models import Wod, Likes

class WodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wod
        fields = ['id', 'name', 'description']

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['id', 'user', 'wod']
