from django.contrib import admin
from .models import DataRecord

# Register your models here.


@admin.register(DataRecord)

class DataRecordAdmin(admin.ModelAdmin):
    list_display = ['id','user','age','salary','result','datetime']
