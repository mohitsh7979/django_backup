from django import forms 
from .models import todolist

class Toform(forms.ModelForm):

    class Meta:

        model = todolist
        fields = ('__all__')