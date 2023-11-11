from django.db import models

# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=20)
    teacher = models.CharField(max_length=50,null=True,blank=True)
    date_time = models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return self.subject_name
    


class student(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)



    
