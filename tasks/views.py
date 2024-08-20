from django.shortcuts import render
import requests
from rest_framework import generics,permissions,views,response,status
from rest_framework.response import Response
from users.models import User
from invites.models import Invites
from .models import Task,TaskProgress
from .serializers import TaskSerializer,TaskProgressSerializer


# Create your views here.
class ListTask(generics.ListAPIView):
    serializer_class=TaskSerializer
    permission_classes=[permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        userId=kwargs['id']
        allTask=Task.objects.all()
        ongoingTask=TaskProgress.objects.filter(user=userId , completed=False).values_list('task_id',flat=True)
        completedTask=TaskProgress.objects.filter(user=userId , completed=True).values_list('task_id',flat=True)
        non_included=allTask.exclude(id__in=ongoingTask).exclude(id__in=completedTask)

        data={"ongoingTask":TaskSerializer(Task.objects.filter(id__in=ongoingTask),many=True).data,"completedTask":TaskSerializer(Task.objects.filter(id__in=completedTask),many=True).data,"non_included":TaskSerializer(non_included,many=True).data}
        
        return Response(data=data,status=status.HTTP_200_OK)

class ListUpdateTask(generics.RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[permissions.AllowAny]

class startTask(views.APIView):
    serializer_class=TaskProgressSerializer

    def post(self,request):
        taskid=request.data.get("task")
        userid=request.data.get("user")
        taskName=Task.objects.get(id=taskid)
        user=User.objects.get(userid=userid)

        if taskid == 4:         # joining bonus
            task=TaskProgress.objects.get_or_create(task=taskName,user=user,completed=True)[0]
            user.totalScore+=taskName.points

        elif taskid == 1:       # invite 1 friend
            task=TaskProgress.objects.get_or_create(task=taskName,user=user)[0]
            if len(Invites.objects.filter(fromUser=userid))>1:
                user.totalScore+=taskName.points
                task.completed=True
                task.save()

        elif taskid == 5:       # invite 5 friend
            task=TaskProgress.objects.get_or_create(task=taskName,user=user)[0]
            if len(Invites.objects.filter(fromUser=userid))>=5:
                user.totalScore+=taskName.points
                task.completed=True
                task.save()

        elif taskid == 6:       # maintain 5 day streak
            task=TaskProgress.objects.get_or_create(task=taskName,user=user)[0]
            if user.streak>=5:
                user.totalScore+=taskName.points
                task.completed=True
                task.save()

        elif taskid == 2:  # telegram add
            ############# METHOD DATA ################
            token="7339703220:AAG_15jrVsq7cTE6MU_2pd9O0s9v1pSGvKs"
            group_id="-4529992520"
            params={"chat_id":group_id,"user_id":userid}
            url=f"https://api.telegram.org/bot{token}/getChatMember"
            
            task,created=TaskProgress.objects.get_or_create(task=taskName,user=user)
            serializer=TaskProgressSerializer(task)
            newData=serializer.data
            print(task,created,userid)

            res=requests.get(url,params)

            if (res.json()['result']['status']=="member" or res.json()['result']['status']=="creator"):
                task.completed=True
                task.save()
                serializer=TaskProgressSerializer(task)
                newData=serializer.data
            else:
                newData['link']="https://t.me/+ql3eKHqtO5IwOWM1"
            return response.Response(newData,status=status.HTTP_201_CREATED)
            


        elif taskid == 3:
            task=TaskProgress.objects.get_or_create(task=taskName,user=user,completed=True)[0]

        elif taskid == 7:
            task=TaskProgress.objects.get_or_create(task=taskName,user=user,completed=True)[0]

        elif taskid == 8:
            task=TaskProgress.objects.get_or_create(task=taskName,user=user,completed=True)[0]

        elif taskid == 9:
            task=TaskProgress.objects.get_or_create(task=taskName,user=user,completed=True)[0]

        elif taskid == "10":
            task=TaskProgress.objects.get_or_create(task=taskName,user=user,completed=True)[0]

        else:
            task=TaskProgress.objects.get_or_create(task=taskName,user=user)[0]


        user.save()
        serializer=TaskProgressSerializer(task)

        return response.Response(serializer.data,status=status.HTTP_201_CREATED)