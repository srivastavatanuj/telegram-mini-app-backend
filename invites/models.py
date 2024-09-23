from django.db import models

# Create your models here.
class Invites(models.Model):
    fromUser=models.BigIntegerField()
    toUser=models.CharField(max_length=150)
    purchase=models.BooleanField(default=False)
    amount=models.IntegerField(default=0)
