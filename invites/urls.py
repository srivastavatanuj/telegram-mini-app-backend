from django.urls import path
from .views import *

urlpatterns = [
    path('create/',createInvite.as_view(),name='createinvites'),
    path('get/<int:pk>/',getInviteData.as_view(),name='getinvites'),
    path('get-referral/<int:pk>/',getReferralData.as_view(),name='getreferral')
]
