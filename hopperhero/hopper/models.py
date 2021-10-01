from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.


class Wod(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    wod = models.ForeignKey(Wod, on_delete=CASCADE)
