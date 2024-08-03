from django.urls import include, path
from .views import *

urlpatterns = [
    path('',GetOrCreateUser.as_view(),name='getUserData'),
    path('leaderboard/',UserLeaderboard.as_view(),name='userleaderboard'),
    path('update/',UpdateUser.as_view(),name='updateUserData'),
]
