from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATE_CHOICES=(
    ('Rajasthan','Rajasthan'),
    ('Haryana','Haryana'),
    ('Delhi','Delhi'),
    ('UP','UP'),
    ('HP','HP'),
    ('Punjab','Punjab'),
    ('Bihar','Bihar'),
    ('MP','Mp'),
    ('Gujarat','Gujrat'),
    ('Chandigarh','Chandigarh'),
    ('Goa','Goa')

)

CITY_CHOICES=(
    ('Jaipur','Jaipur'),
    ('Udaipur','Udaipur'),
    ('Ajmer','Ajmer'),
    ('Badmer','Badmer'),
    ('Dosa','Dosa')
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    First_name=models.CharField(max_length=100) # first_name
    last_name=models.CharField(max_length=100)
    Email_id=models.EmailField() #email_id
    address=models.CharField(max_length=500)
    land_mark=models.CharField(max_length=100)
    State=models.CharField(choices=STATE_CHOICES,max_length=100)
    City=models.CharField(choices=CITY_CHOICES,max_length=100)
    pin_code=models.IntegerField()
    Mobile_no=models.IntegerField()

