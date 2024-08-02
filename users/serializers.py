from rest_framework import serializers
from .models import User,Task

class UserSerializer(serializers.Serializer):
    class Meta:
        model=User
        fields="__all__"

class TaskSerializer(serializers.Serializer):
    class Meta:
        model=Task
        fields="__all__"