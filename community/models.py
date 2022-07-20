from django.db import models

# Create your models here.
class Community(models.Model):
    issueRoom = models.CharField(max_length=20)
    issueProf = models.CharField(max_length=50)
    issueName = models.CharField(max_length=20)
    issueContent = models.TextField()
    issueTime = models.TimeField()