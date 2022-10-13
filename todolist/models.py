from email.policy import default
from time import timezone
from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    isFinished = models.BooleanField(default=False)
