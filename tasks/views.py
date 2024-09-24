from django.shortcuts import render
import requests
from rest_framework import generics, permissions, views, response, status
from rest_framework.response import Response
from users.models import User
from .models import Task, TaskProgress
from invites.models import Invites
from .serializers import TaskSerializer, TaskProgressSerializer

# Create your views here.
class ListTask(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        userId = kwargs['id']
        allTask = Task.objects.all()
        ongoingTask = TaskProgress.objects.filter(user=userId, completed=False).values_list('task_id', flat=True)
        completedTask = TaskProgress.objects.filter(user=userId, completed=True).values_list('task_id', flat=True)
        non_included = allTask.exclude(id__in=ongoingTask).exclude(id__in=completedTask)

        data = {
            "ongoingTask": TaskSerializer(Task.objects.filter(id__in=ongoingTask), many=True).data,
            "completedTask": TaskSerializer(Task.objects.filter(id__in=completedTask), many=True).data,
            "non_included": TaskSerializer(non_included, many=True).data
        }

        return Response(data=data, status=status.HTTP_200_OK)

class ListUpdateTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

class ListAllTask(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

class startTask(views.APIView):
    serializer_class = TaskProgressSerializer

    def post(self, request):
        taskid = request.data.get("task")
        userid = request.data.get("user")
        taskName = Task.objects.get(id=taskid)
        user = User.objects.get(userid=userid)

        if taskid == 1:  # joining bonus
            task = TaskProgress.objects.get_or_create(task=taskName, user=user, completed=True)[0]
            user.totalScore += taskName.points

        elif taskid == 2:  # invite 1 friend
            task = TaskProgress.objects.get_or_create(task=taskName, user=user)[0]
            if len(Invites.objects.filter(fromUser=userid)) >= 1:
                user.totalScore += taskName.points
                task.completed = True
                task.save()

        elif taskid == 3:  # telegram add
            ############# METHOD DATA ################
            token = "6710353482:AAE0w4u2SdSpETEq_jdptnUplZSiYXmL3VI"
            group_id = "-1002142412482"
            params = {"chat_id": group_id, "user_id": userid}
            url = f"https://api.telegram.org/bot{token}/getChatMember"

            task, created = TaskProgress.objects.get_or_create(task=taskName, user=user)
            serializer = TaskProgressSerializer(task)
            newData = serializer.data
            print(task, created, userid)

            res = requests.get(url, params)

            if res.json()['result']['status'] in ["member", "creator"]:
                task.completed = True
                task.save()
                user.totalScore += taskName.points
                user.save()
                serializer = TaskProgressSerializer(task)
                newData = serializer.data
            else:
                newData['link'] = "https://t.me/rapidrush/"
            return response.Response(newData, status=status.HTTP_201_CREATED)

        elif taskid == 4:  # twitter page
            # Get or create the task progress record
            task, created = TaskProgress.objects.get_or_create(task=taskName, user=user)
            serializer = TaskProgressSerializer(task)
            newData = serializer.data

            # If the task is just being started (first click)
            if not task.completed and created:
                # Provide the Twitter link
                newData['link'] = "https://x.com/RapidRushXYZ"
            elif not task.completed and not created:
                # If the task was already started and the user is returning to claim the points
                user.totalScore += taskName.points
                user.save()
                task.completed = True
                task.save()

            return response.Response(newData, status=status.HTTP_201_CREATED)

        elif taskid == 5:  # invite 3 friend
            task = TaskProgress.objects.get_or_create(task=taskName, user=user)[0]
            if len(Invites.objects.filter(fromUser=userid)) >= 3:
                user.totalScore += taskName.points
                task.completed = True
                task.save()

        elif taskid == 6:  # maintain 5 day streak
            task = TaskProgress.objects.get_or_create(task=taskName, user=user)[0]
            if user.streak >= 5:
                user.totalScore += taskName.points
                task.completed = True
                task.save()

        elif taskid == 7:
            task = TaskProgress.objects.get_or_create(task=taskName, user=user, completed=True)[0]

        elif taskid == 8:
            task = TaskProgress.objects.get_or_create(task=taskName, user=user, completed=True)[0]

        elif taskid == 9:
            task = TaskProgress.objects.get_or_create(task=taskName, user=user, completed=True)[0]

        elif taskid == "10":
            task = TaskProgress.objects.get_or_create(task=taskName, user=user, completed=True)[0]

        else:
            task = TaskProgress.objects.get_or_create(task=taskName, user=user)[0]

        user.save()
        serializer = TaskProgressSerializer(task)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

class gameTask(generics.UpdateAPIView):
    queryset=User.objects.all()
    serializer_class=GamePointsSerializer
    permission_classes=[permissions.AllowAny]

    def update(self, request, *args, **kwargs):
        userid=request.data['userid']
        score=request.data['totalScore']

        try:
            user=User.objects.get(userid=int(userid))
            user.totalScore+=int(score)
           
        except:
            return response.Response({'error':"invalid user id"})
        user.save()
        return response.Response({"success":"points updated"})
