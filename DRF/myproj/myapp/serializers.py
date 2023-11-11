from rest_framework import serializers
from .models import student,Subject


class RegisterSeralizer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subject
        fields = ('__all__')


class StudentSerializer(serializers.ModelSerializer):
    subject  = SubjectSerializer()
    class Meta:

        model = student
        fields = ('__all__')
        # depth = 1