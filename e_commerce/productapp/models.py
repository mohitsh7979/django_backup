from django.db import models
from django.contrib.auth.models import User
from authenticationapp.models import Customer

# Create your models here.

CATEGORY_CHOICES=(
    ('m','men'),
    ('w','women'),
    ('k','kids'),
    ('mk','men kit'),
    ('wt','watch'),
    ('f','featured_product'),
    ('l','latest_product'),
    ('b','brands'),
    ('t','testimonial'),
    ('o','offers'),
    ('ban','banner'),
    
)

# BRAND_CHOICES=(
#     ('p','paint'),
#     ('j','jeans'),
#     ('t','t-shirt'),
#     ('s','shirt'),
#     ('T','toper')
  
# )


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=1000)
    catagory = models.CharField(choices=CATEGORY_CHOICES,max_length=50)
    # brand=models.CharField(choices=BRAND_CHOICES,max_length=50,default=1)
    images = models.ImageField(upload_to='media/productimages')
    color = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=15, null=True, blank=True)
   
    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


class Orderplaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    quantity = models.CharField(max_length=100)




# STATE_CHOICES=(
#     ('Rajasthan','Rajasthan'),
#     ('Haryana','Haryana'),
#     ('Delhi','Delhi'),
#     ('UP','UP'),
#     ('HP','HP'),
#     ('Punjab','Punjab'),
#     ('Bihar','Bihar'),
#     ('MP','Mp'),
#     ('Gujarat','Gujrat'),
#     ('Chandigarh','Chandigarh'),
#     ('Goa','Goa')

# )

# CITY_CHOICES=(
#     ('Jaipur','Jaipur'),
#     ('Udaipur','Udaipur'),
#     ('Ajmer','Ajmer'),
#     ('Badmer','Badmer'),
#     ('Dosa','Dosa')
# )

# class Customer(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     First_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     Email_id=models.EmailField()
#     address=models.CharField(max_length=500)
#     land_mark=models.CharField(max_length=100)
#     State=models.CharField(choices=STATE_CHOICES,max_length=100)
#     City=models.CharField(choices=CITY_CHOICES,max_length=100)
#     pin_code=models.IntegerField()
#     Mobile_no=models.IntegerField()

