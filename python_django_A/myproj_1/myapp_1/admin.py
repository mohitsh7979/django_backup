from django.contrib import admin
from .models import student,form_data

# Register your models here.

admin.site.register(student)

@admin.register(form_data)

class Myadmin(admin.ModelAdmin):
    list_display = ['id','name','email','address']



