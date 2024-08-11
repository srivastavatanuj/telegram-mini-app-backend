from datetime import datetime
from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.views import APIView
from .models import *
from .serializers import *
from invites.models import *
from rest_framework.response import Response
from rest_framework import status
from datetime import date   

# Create your views here.
class GetOrCreateUser(APIView):
    def post(self,request):
        userid=request.data.get('userid')
        username=request.data.get('username')
        referby=request.data.get('referBy')

        user=User.objects.filter(userid=userid).first()

        if user:
            if (date.today() - user.lastlogin).days==0:
                pass
            elif (date.today() - user.lastlogin).days==1:
                user.streak+=1
                user.totalScore+=user.streak*10
            else:
                user.streak=0

            user.lastlogin=date.today()
            user.save()
            serializer=UserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        if(referby):
            Invites.objects.create(fromUser=referby,toUser=username)
            user=User.objects.get(userid=referby)
            user.totalScore+=50
            user.save()

        user=User.objects.create(userid=userid,username=username)
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class UserLeaderboard(generics.ListAPIView):
    
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]

    def get_queryset(self):
        queryset=User.objects.all().order_by("-totalScore")
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)
        userid=kwargs['userid']
        rank=list(queryset).index(queryset.get(userid=userid))+1

        data={'data':serializer.data,"rank":rank}
        return Response(data, status=status.HTTP_200_OK)


class UpdateUser(generics.UpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]



