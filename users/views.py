from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.views import APIView
from .models import *
from .serializers import *
from invites.models import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class GetOrCreateUser(APIView):
    def post(self,request):
        userid=request.data.get('userid')
        username=request.data.get('username')
        referby=request.data.get('referBy')

        

        user=User.objects.filter(userid=userid).first()

        if user:
            serializer=UserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        if(referby):
            Invites.objects.create(fromUser=referby,toUser=username)

        user=User.objects.create(userid=userid,username=username)
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class UserLeaderboard(generics.ListAPIView):
    
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]

    def get_queryset(self):
        queryset=User.objects.all().order_by("-totalScore")
        return queryset


class UpdateUser(generics.UpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]



