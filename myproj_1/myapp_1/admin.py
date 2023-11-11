from django.contrib import admin
from .models import student_models

# Register your models here.

@admin.register(student_models)

class Student_Admin(admin.ModelAdmin):
    list_display = ['name','email','mobile_no','skills','image']
