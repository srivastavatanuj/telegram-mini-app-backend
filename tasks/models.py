from django.db import models
from users.models import *

# Create your models here.
class TaskEntry(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    date=models.DateField(auto_now=True)