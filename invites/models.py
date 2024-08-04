from django.db import models

# Create your models here.
class Invites(models.Model):
    fromUser=models.IntegerField()
    toUser=models.CharField(max_length=150)