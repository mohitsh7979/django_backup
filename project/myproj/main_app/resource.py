from import_export import resources 
from .models import ProjectTable

class ReportResource(resources.ModelResource):
     class Meta:
         model = ProjectTable