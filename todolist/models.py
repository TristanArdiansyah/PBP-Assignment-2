from turtle import title
from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = date.today()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    isFinished = models.BooleanField(default=False)
