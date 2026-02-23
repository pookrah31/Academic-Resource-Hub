from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    department = models.CharField(max_length=100, blank=True)
    level = models.IntegerField(null=True, blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png', null=True, blank=True)
    contribution_points = models.IntegerField(default=0)