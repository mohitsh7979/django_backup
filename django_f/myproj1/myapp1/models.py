from django.db import models

# Create your models here.


class contact_detail(models.Model):
    email = models.EmailField()
    description = models.TextField(max_length=500)


class todolist(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    
