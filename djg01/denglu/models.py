from django.db import models
# from django.contrib.auth.models import User, AbstractUser, auth

class UserInfo(models.Model):
    username=models.CharField(max_length=128)
    password=models.CharField(max_length=128)
