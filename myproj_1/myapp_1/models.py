from django.db import models

# Create your models here.

class student_models(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    mobile_no = models.CharField(max_length=10)
    skills = models.CharField(max_length = 50)
    image = models.ImageField(max_length = 50)



class s_model(models.Model):
    name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)