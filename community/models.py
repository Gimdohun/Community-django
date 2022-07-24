from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Issue(models.Model):
    room = models.CharField(max_length=20)
    prof = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    content = models.TextField()
    time = models.TimeField()
    
class UserInfo(models.Model):
    name = models.CharField(max_length=15, validators=[MinLengthValidator(3)])
    email = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
    userID = models.CharField(max_length=15, validators=[MinLengthValidator(6)])
    userPW = models.CharField(max_length=15, validators=[MinLengthValidator(8)])
    reUserPW = models.CharField(max_length=15, validators=[MinLengthValidator(8)], null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=20)
    host = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True)



