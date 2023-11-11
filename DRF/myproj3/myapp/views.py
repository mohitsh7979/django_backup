from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.serializers import StudentSerializer
from .models import student
from rest_framework.views import APIView
from myapp.serializers import RegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.



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


class Register(APIView):

    def post(self,request):

        data  = request.data 
        print(data,'>>>>>>>>>data')
        serialize_data = RegisterSerializer(data=data)
        if not serialize_data.is_valid():
            return Response({

                'status':False,
                'message':serialize_data.errors,
            },status.HTTP_400_BAD_REQUEST)
        
        else:

            serialize_data.save()
            return Response({

                'status':True,
                'message':'user account created',
            },status.HTTP_201_CREATED)
        

class Login(APIView):

    def post(self,request):

        data = request.data 
        print(data,'>>>>>>>>>>')
        serialize_data = LoginSerializer(data=data)
        if not serialize_data.is_valid():
            return Response({

                'status':False,
                'message':serialize_data.errors,
            },status.HTTP_400_BAD_REQUEST)
        
        else:

            user = authenticate(username = serialize_data.data['username'] , password = serialize_data.data['password'])

            print(user,'>>>>>>>>>>>>user    ')

            if user is None:
                return Response({

                'status':False,
                'message':'invalid',
                },status.HTTP_400_BAD_REQUEST)
            
            else:

                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                return Response({

                    'status':True,
                    'token':str(token)
                },status.HTTP_200_OK)

        


        
