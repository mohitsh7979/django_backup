from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from myapp.serializers import EmployeeSerializer


@api_view(['GET','POST'])
def index(request):

    if request.method == "POST":
        
        api_data = request.data 
        global name , age , city , desg
        name = api_data['Name']
        age = api_data['Age']
        city = api_data['City']
        desg = api_data['Designation']
        return Response(api_data)
    
    if request.method == "GET":
        context = {

            'Name':name,
            'Age':age,
            'City':city,
            'Designation':desg
        }
        print(request.GET.get('search'))
        return Response(context)
    
    
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def employee(request):

    if request.method == 'GET':

        data = Employee.objects.all()
        dataserializer = EmployeeSerializer(data,many = True)
        print(dataserializer)
        return Response(dataserializer.data)
    
    elif request.method == 'POST':

        data = request.data
        dataserializer = EmployeeSerializer(data=data)
        print(dataserializer)

        if dataserializer.is_valid():
            dataserializer.save()
            return Response(data)
        
    elif request.method == 'PUT':

        data = request.data
        dataserializer = EmployeeSerializer(data=data)
        print(dataserializer)

        if dataserializer.is_valid():
            dataserializer.save()
            return Response(data)
        
    elif request.method == 'PATCH':

        data = request.data
        obj_data = Employee.objects.get(id = data['id'])
        dataserializer = EmployeeSerializer(obj_data , data=data , partial = True)
        print(dataserializer)

        if dataserializer.is_valid():
            dataserializer.save()
            return Response(dataserializer.data)
        
        return Response(dataserializer.errors)
    
    else:

        data = request.data 
        obj_data = Employee.objects.get(id = data['id'])
        print(obj_data)
        obj_data.delete()
        return Response({'message':'Deleted this entery'})



    

    
