from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Task,TaskProgress
from users.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"

class TaskProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskProgress
        fields="__all__"

class GamePointsSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['userid','totalScore']