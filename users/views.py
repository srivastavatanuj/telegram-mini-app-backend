from datetime import datetime, date
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from invites.models import Invites
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum


# Create your views here.
class GetOrCreateUser(APIView):
    def post(self, request):
        userid = request.data.get('userid')
        username = request.data.get('username')
        referby = request.data.get('referBy')

        # Validate username
        if not username:
            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(userid=userid).first()
        showStreak = True

        if user:
            if (date.today() - user.lastlogin).days == 0:
                showStreak = False
            elif (date.today() - user.lastlogin).days == 1:
                user.streak += 1
                user.totalScore += user.streak * 10
            else:
                user.streak = 1

            user.lastlogin = date.today()
            user.save()
            serializer = UserSerializer(user)
            newData = serializer.data
            newData['showStreak'] = showStreak  # type: ignore
            return Response(newData, status=status.HTTP_200_OK)

        # If 'referby' is provided, handle the invite and update the referring user's score
        if referby:
            Invites.objects.create(fromUser=referby, toUser=username)
            referring_user = User.objects.get(userid=referby)
            referring_user.totalScore += 50
            referring_user.save()

        # Create a new user with the provided 'userid' and 'username'
        user = User.objects.create(userid=userid, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLeaderboard(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = User.objects.all().order_by("-totalScore")
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        userid = kwargs.get('userid', None)
        try:
            rank = list(queryset).index(queryset.get(userid=userid)) + 1
            allPoints=User.objects.aggregate(totalScore=Sum('totalScore'))
            data = {'data': serializer.data, "rank": rank,"totalScore":allPoints['totalScore']}
        except User.DoesNotExist:
            data = {'data': serializer.data}
        return Response(data, status=status.HTTP_200_OK)

class UpdateUser(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
