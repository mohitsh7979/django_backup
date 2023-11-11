from django.contrib import admin
from .models import ProjectTable
from import_export.admin import ImportExportModelAdmin
from .resource import ReportResource 

# Register your models here.

class ReportAdmin(ImportExportModelAdmin):
     resource_class = ReportResource

admin.site.register(ProjectTable,ReportAdmin)

# @admin.register(ProjectTable)

# class ProjectTableAdmin(admin.ModelAdmin):
#     list_display = ['id','project_name','proejct_link','updated_date']
