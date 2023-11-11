from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
     
    def validate(self, data):

        if data['username']:

            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('username already taken')
            
        if data['email']:

            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email already taken')
        
        return data
            
    def create(self,data):
        user = User.objects.create(username=data['username'],email=data['email'])
        user.set_password(data['password'])
        user.save()
        return data
    

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()



from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Employee
        fields = ('__all__')
