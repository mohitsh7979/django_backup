from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.serializers import StudentSerializer,RegisterSeralizer
from .models import student
from rest_framework.views import APIView

# Create your views here.


class StudentAPi(APIView):

    def get(self,request):
        data = student.objects.all()
        serializer_data = StudentSerializer(data,many=True)
        return Response(serializer_data.data)
        

    def post(self,request):
        data  = request.data 
        serializer_data = StudentSerializer(data=data)

        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
    
    def put(self,request):
        data  = request.data 
        serializer_data = StudentSerializer(data=data)

        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)

    def patch(self,request):
        data  = request.data 
        data_id = request.data['id']
        data_obj = student.objects.get(id=data_id)
        serializer_data = StudentSerializer(data_obj,data=data,partial=True)

        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)

    def delete(self,request):
        data_id = request.data['id']
        obj_data = student.objects.get(id=data_id) 
        obj_data.delete()
        return Response({'message':'data deleted'})



@api_view(['GET','POST','DELETE','PUT','PATCH'])
def index(request):
    
    if request.method == 'GET':

        data = student.objects.all()
        serializer_data = StudentSerializer(data,many=True)
        return Response(serializer_data.data)

    elif request.method == 'POST':

        data  = request.data 
        serializer_data = StudentSerializer(data=data)

        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
        
    elif request.method == 'PUT':

        data  = request.data 
        serializer_data = StudentSerializer(data=data)

        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
        
    elif request.method == 'PATCH':

        data  = request.data 
        data_id = request.data['id']
        data_obj = student.objects.get(id=data_id)
        serializer_data = StudentSerializer(data_obj,data=data,partial=True)

        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
        
    elif request.method == 'DELETE':

        data_id = request.data['id']

        obj_data = student.objects.get(id=data_id) 
        obj_data.delete()
        return Response({'message':'data deleted'})
    

@api_view(['POST'])
def regeister(request):
    data = request.data 
    print(data,'>>>>>>>>>>')
    serilaizer_data = RegisterSeralizer(data=data)

    if serilaizer_data.is_valid():
        data = serilaizer_data.validated_data
        return Response({'message':'success'})
    
    return Response(serilaizer_data.errors)



        
