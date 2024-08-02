from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    username=models.PositiveIntegerField(primary_key=True)
    wallet=models.CharField(unique=True,blank=True)
    dateTime=models.DateField(auto_now_add=True)
    totalScore=models.PositiveIntegerField(default=0)
    invites=models.PositiveIntegerField(default=0)
    lastlogin=models.DateField(auto_now_add=True)


class Task(models.Model):
    name = models.CharField(
        max_length=255,
        validators=[RegexValidator(regex=r'^.{4,}$', message='Name must be at least 4 characters long.')]
    )
    points=models.PositiveIntegerField(default=0)
    icon=models.ImageField(upload_to='icons',blank=True)