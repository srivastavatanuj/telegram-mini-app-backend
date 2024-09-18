from django.shortcuts import render
from rest_framework import generics,permissions,response
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
    
class getReferralData(generics.ListAPIView):
    serializer_class=InviteSerializer
    permission_classes=[permissions.AllowAny]
    
    def get(self, request, *args, **kwargs):
        bonusPercent=10
        pk=self.kwargs['pk']
        totalInvites=Invites.objects.filter(fromUser=pk).count()
        purchaseCount=Invites.objects.filter(fromUser=pk,purchase=True).count()
        bonusAmount=Invites.objects.filter(fromUser=5870351809,purchase=True).values_list('amount',flat=True)
        data={"totalInvites":totalInvites,"purchaseCount":purchaseCount,"bonusAmount":(sum(bonusAmount)/bonusPercent),"bonusPercent":f"{bonusPercent}%"}
        return response.Response(data)
    