from django import forms  
from django.contrib.auth.forms import PasswordResetForm



class resetform(PasswordResetForm):
    email =  forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control u','placeholder':'Enter Your Email id'}))