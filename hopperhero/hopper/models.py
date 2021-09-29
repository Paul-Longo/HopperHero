from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wod(models.Model):
    users = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

class Likes(models.Model):
    users = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    like = models.ManyToManyField(Wod)