from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    userid=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=150)
    wallet=models.CharField(blank=True,max_length=150)
    dateTime=models.DateField(auto_now_add=True)
    totalScore=models.PositiveIntegerField(default=0)
    lastlogin=models.DateField(default=datetime.now)
    streak=models.IntegerField(default=0)

    def __str__(self):
        return self.username