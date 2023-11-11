from django.shortcuts import render
from rest_framework.views import APIView
from myapp.serializers import RegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.


class RegisterAccount(APIView):

    def post(self,request):

        data = request.data
        data_serializer = RegisterSerializer(data=data)

        if not data_serializer.is_valid():
            return Response({

                'status':False,
                'message':data_serializer.errors,
            },status.HTTP_400_BAD_REQUEST)
        
        else:

            data_serializer.save()
            return Response({
                
                'status':True,
                'message':'user account created',
            },status.HTTP_201_CREATED)



class LoginAccount(APIView):

    def post(request):

        data  = request.data 
        data_serializer = LoginSerializer(data=data)
        if not data_serializer.is_valid():
            return Response({

                'status':False,
                'message':data_serializer.errors,
            },status.HTTP_400_BAD_REQUEST)
        
        else:
            user  = authenticate(username = data_serializer.data['username'],password = data_serializer.data['password'])

            if user is None:
                return Response({

                    'status':False,
                    'message':'invalid',
                },status.HTTP_400_BAD_REQUEST)
            
            token , _ = Token.objects.get_or_create(user=user)
            print(token)
            
        
        

        
