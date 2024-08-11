from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class ListTask(generics.ListAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[permissions.AllowAny]

class ListUpdateTask(generics.RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[permissions.AllowAny]