from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

# class Customer(forms.Form):
#     First_name=forms.CharField()
#     Last_name=forms.CharField()
#     Email_id=forms.EmailField()


class Register(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confrim Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})}


class customer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["First_name", "last_name", "address",
                  "pin_code", "Mobile_no", "State", "City"]
        widgets = {
               'First_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control'}),
            'Mobile_no': forms.TextInput(attrs={'class': 'form-control'}),

        }
