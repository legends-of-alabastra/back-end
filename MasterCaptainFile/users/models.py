from django.db import models
# from . import UserSerializer
# Create your models here.
class UserInfo(models.Model):
    id =  models.IntegerField(default = 0, primary_key=True)
    username  = models.CharField(max_length=255, default="DEFAULT DESCRIPTION", unique= True)
    gold = models.IntegerField(default = 0)
    gem = models.IntegerField(default = 0)

    def __str__(self):
        return self.username
