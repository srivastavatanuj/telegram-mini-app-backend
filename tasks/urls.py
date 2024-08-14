from django.urls import path
from .views import *


urlpatterns = [
    path('<int:id>/',ListTask.as_view(),name='task'),
    path('starttask/',startTask.as_view(),name='task'),
]
