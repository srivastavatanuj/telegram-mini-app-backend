from django.db import models
from users.models import *
from django.core.validators import RegexValidator

# Create your models here.

class Task(models.Model):
    name = models.CharField(
        max_length=255,
        validators=[RegexValidator(regex=r'^.{4,}$', message='Name must be at least 4 characters long.')]
    )
    points=models.PositiveIntegerField(default=0)
    icon=models.ImageField(upload_to='icons',blank=True)

    def __str__(self):
        return self.name


class TaskProgress(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    date=models.DateField(auto_now=True)