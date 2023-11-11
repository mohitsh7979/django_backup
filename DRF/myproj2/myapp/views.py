from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Teacher
from myapp.serializer import TeacherSerializer

# Create your views here.


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def teacher(request):

    if request.method == 'GET':
        data_obj = Teacher.objects.all()
        serializer_obj = TeacherSerializer(data_obj , many = True)
        return Response(serializer_obj.data)
    
    
    elif request.method == 'POST':

        data = request.data
        serializer_obj = TeacherSerializer(data=data)

        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        
        
    elif request.method == 'PUT':

        data = request.data
        serializer_obj = TeacherSerializer(data=data)

        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)


    
    elif request.method == 'PATCH':

        data = request.data
        data_id = request.data['id']
        data_obj = Teacher.objects.get(id=data_id)
        data_serializer = TeacherSerializer(data_obj,data=data,partial=True)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response(data_serializer.data)
    
    else:
        data = request.data
        data_id = request.data['id']
        data_obj = Teacher.objects.get(id=data_id)
        data_obj.delete()
        return Response({'message':'data deleted'})
        

        








