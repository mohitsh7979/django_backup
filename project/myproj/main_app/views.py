from django.shortcuts import render
from .models import ProjectTable
# Create your views here.

def project_table_data(request):

    data = ProjectTable.objects.all()
    print(data)

    return render(request,'main_app/table.html',{'data':data})

