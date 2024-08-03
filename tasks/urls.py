from django.urls import path
from .views import *


urlpatterns = [
    path('',CreateListTask.as_view(),name='task')
]
