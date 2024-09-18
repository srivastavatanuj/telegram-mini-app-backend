from django.db import models

# Create your models here.
class Invites(models.Model):
    fromUser=models.IntegerField()
    toUser=models.CharField(max_length=150)
    purchase=models.BooleanField(default=False)
    amount=models.IntegerField(default=0)
