from rest_framework import serializers
from .models import Teacher,Color


class ColorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Color
        fields = ('__all__')




class TeacherSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_code  = serializers.SerializerMethodField()

    class Meta:

        model = Teacher
        fields = ('__all__')
        # depth = 1

    def get_color_code(self,obj):
        color_obj = Color.objects.get(id=obj.color.id)
        print(color_obj)
        return {

            'color_name':color_obj.color_name,
            'hexa_code':'#f57886'
        }
        


    def validate(self,data):
            
        print(data['age'])

        if data['age'] < 18:
            raise serializers.DjangoValidationError("Age should be grater than 18")
            
        return data