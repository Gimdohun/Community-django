from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

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
    
class UserInfo(models.Model):
    Name = models.CharField(max_length=15, validators=[MinLengthValidator(3)])
    Email = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
    UserID = models.CharField(max_length=15, validators=[MinLengthValidator(6)])
    UserPW = models.CharField(max_length=15, validators=[MinLengthValidator(8)])
    ReUserPW = models.CharField(max_length=15, validators=[MinLengthValidator(8)], null=True)


