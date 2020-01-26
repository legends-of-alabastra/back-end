from django.db import models

# Create your models here.

class UserInfo(models.Model):
        username  = models.CharField(max_length=255, default="DEFAULT DESCRIPTION")
        gold = models.IntegerField(default = 0)
        gem = models.IntegerField(default = 0)

        def __str__(self):
            return self.username