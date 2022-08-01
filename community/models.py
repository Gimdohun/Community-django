from django.db import models
from django.conf import settings

# Create your models here.
class Issue(models.Model):
    room = models.CharField(max_length=20)
    prof = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    content = models.TextField()
    time = models.TimeField()

class Room(models.Model):
    name = models.CharField(max_length=20)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)



