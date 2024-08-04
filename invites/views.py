from django.shortcuts import render
from rest_framework import generics,permissions
from .models import * 
from .serializers import InviteSerializer
# Create your views here.


class createInvite(generics.CreateAPIView):
    queryset=Invites.objects.all()
    serializer_class=InviteSerializer
    permission_classes=[permissions.AllowAny]

class getInviteData(generics.ListAPIView):
    serializer_class=InviteSerializer
    permission_classes=[permissions.AllowAny]

    def get_queryset(self):
        pk=self.kwargs['pk']
        queryset=Invites.objects.filter(fromUser=pk)
        return queryset