from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=20)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Issue(models.Model):
    Room = models.CharField(max_length=20)
    Prof = models.CharField(max_length=50)
    Name = models.CharField(max_length=20)
    Content = models.TextField()
    Time = models.TimeField()


