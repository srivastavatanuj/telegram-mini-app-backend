from django.urls import path
from .views import ListAllTask, ListTask, startTask, gameTask

urlpatterns = [
    path('all/', ListAllTask.as_view(), name='alltask'),
    path('<int:id>/', ListTask.as_view(), name='task'),
    path('starttask/', startTask.as_view(), name='starttask'),
    path('updategamepoints/', gameTask.as_view(), name='gametask'),
]
