from django.db import models
from django.contrib.auth.models import User, AbstractUser, auth


# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=128)
    password=models.CharField(max_length=128)
# Create your models here.
class fkuser(User):
    pass

class stser(AbstractUser):
    nick_name = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass

