from rest_framework import serializers
from .models import Task,TaskProgress

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"

class TaskProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskProgress
        fields="__all__"