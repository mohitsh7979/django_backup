from django.db import models

# Create your models here.

class ProjectTable(models.Model):
    project_name = models.CharField(max_length=100)
    proejct_link = models.CharField(max_length=100)
    updated_date = models.DateTimeField()


    def __str__(self):
        return self.project_name

