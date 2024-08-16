from django.shortcuts import render
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


        if taskid == "1":         # joining bonus
            task=TaskProgress.objects.create(task=taskName,user=user,completed=True)

        elif taskid == "2":       # invite 1 friend
            if len(Invites.objects.filter(FromUser=userid))>1:
                task=TaskProgress.objects.create(task=taskName,user=user,completed=True)
            else:
                task=TaskProgress.objects.create(task=taskName,user=user)

        elif taskid == "3":       # invite 5 friend
            if len(Invites.objects.filter(FromUser=userid))>=5:
                task=TaskProgress.objects.create(task=taskName,user=user,completed=True)
            else:
                task=TaskProgress.objects.create(task=taskName,user=user)

        elif taskid == "4":       # maintain 5 day streak
            if user.streak>=5:
                task=TaskProgress.objects.create(task=taskName,user=user,completed=True)
            else:
                task=TaskProgress.objects.create(task=taskName,user=user)

        elif taskid == "5":
            task=TaskProgress.objects.create(task=taskName,user=user,completed=True)

        elif taskid == "6":
            task=TaskProgress.objects.create(task=taskName,user=user,completed=True)

        elif taskid == "7":
            task=TaskProgress.objects.create(task=taskName,user=user,completed=True)

        elif taskid == "8":
            task=TaskProgress.objects.create(task=taskName,user=user,completed=True)

        elif taskid == "9":
            task=TaskProgress.objects.create(task=taskName,user=user,completed=True)

        elif taskid == "10":
            task=TaskProgress.objects.create(task=taskName,user=user,completed=True)

        else:
            task=TaskProgress.objects.create(task=taskName,user=user)


        user.totalScore+=taskName.points
        user.save()
        serializer=TaskProgressSerializer(task)

        return response.Response(serializer.data,status=status.HTTP_201_CREATED)