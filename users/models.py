from django.db import models


# Create your models here.
class User(models.Model):
    userid=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=150)
    wallet=models.CharField(blank=True,max_length=150)
    dateTime=models.DateField(auto_now_add=True)
    totalScore=models.PositiveIntegerField(default=0)
    lastlogin=models.DateField(auto_now_add=True)
    streak=models.IntegerField(default=0)

