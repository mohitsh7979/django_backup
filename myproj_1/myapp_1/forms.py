from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class resgister_form(UserCreationForm):

    class Meta : 
        model = User
        fields = ['username','email']
        widgets = {

            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'})
        }


class student_forms(forms.Form):
    name = forms.CharField()
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    mobile_no = forms.CharField()
    skills = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Skiils'}))
    image = forms.ImageField(required=True,widget=forms.FileInput(attrs={'class':'form-control'}))


class s_form(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}))
    mobile_no = forms.CharField(max_length=10,required=True,widget=forms.TextInput( attrs= {'class':'form-control','placeholder':'Mobile No'}))
