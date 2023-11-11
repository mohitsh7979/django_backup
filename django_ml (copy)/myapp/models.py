from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class DataRecord(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    age = models.IntegerField()
    salary = models.CharField(max_length=100)
    result = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)


