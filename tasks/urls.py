from django.urls import path
from .views import *


urlpatterns = [
    path('',ListTask.as_view(),name='task')
]
