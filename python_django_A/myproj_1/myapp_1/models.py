from django.db import models

# Create your models here.



class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile_no = models.IntegerField(max_length=10)
    pin_code = models.IntegerField()
    address = models.CharField(max_length=50)

class form_data(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)



class myprofile(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    roll_no = models.IntegerField()
    stream = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=6)
    gender = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media',null = True)
    descripation = models.CharField(max_length=400)


 
    


