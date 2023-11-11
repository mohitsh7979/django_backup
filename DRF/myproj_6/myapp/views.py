from django.shortcuts import render
from rest_framework.views import APIView
from myapp.serializers import RegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from myapp.serializers import EmployeeSerializer
from .models import Employee
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Register(APIView):


    def post(self,request):

        data  = request.data 
        serialize_data = RegisterSerializer(data=data)
        if not serialize_data.is_valid():
            print('i Am in')
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
            


class Data(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        data = Employee.objects.all()
        dataserializer = EmployeeSerializer(data,many = True)
        print(dataserializer)
        return Response(dataserializer.data)

    def post(self,request):

        data = request.data
        dataserializer = EmployeeSerializer(data=data)
        print(dataserializer)

        if dataserializer.is_valid():
            dataserializer.save()
            return Response(data)
  

        
    
