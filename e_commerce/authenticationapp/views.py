from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# from .forms import Customer

# Create your views here.


def Customer_details(request): #functions name are camel case in lower laters.

    if request.method == "POST":
        a = customer(request.POST)
        if a.is_valid():
            usr = request.user
            print(usr)
            first_name = a.cleaned_data['First_name']
            last_name = a.cleaned_data['last_name']
            address = a.cleaned_data['address']
            state = a.cleaned_data['State']
            city = a.cleaned_data['City']
            pin = a.cleaned_data['pin_code']
            mobile = a.cleaned_data['Mobile_no']
            m = Customer(
                user=usr, First_name=first_name, last_name=last_name,
                address=address, State=state, City=city,
                pin_code=pin, Mobile_no=mobile
            )
            m.save()
            return redirect("/")
    else:
        a = customer()
    print(a)
    context = {
        'a': a
    }
    return render(request, 'authenticationapp/customer.html', context)


def register(request):
    if request.method == "POST":
        a = Register(request.POST)
        if a.is_valid():
            messages.success(
                request, 'congratulations!! your account succefully created')
            a.save()
            if a.is_valid():
               uname = a.cleaned_data['username']
               pas = a.cleaned_data['password1']
               print(uname)
               print(pas)
               user = authenticate(username=uname, password=pas)

               if user is not None:
                 login(request, user)

            return redirect("/auth/Customer/")
    else:
        a = Register()
    print(a)
    context = {
        'a': a
    }
    return render(request, 'authenticationapp/register.html', context)


def loginhandle(request):

    #   if request.method=="POST":
    #     # a=AuthenticationForm(request=request,data=request.POST)
    #     # if a.is_valid():
    #         uname=request.POST['username']
    #         pas=request.POST['password']
    #         print(uname)
    #         print(pas)
    #         user=authenticate(username=uname,password=pas)

    #         if user is not None:
    #             login(request,user)

    #   return render(request,'authenticationapp/login.html')

    if request.method == "POST":
        a = AuthenticationForm(request=request, data=request.POST)
        if a.is_valid():
            uname = a.cleaned_data['username']
            pas = a.cleaned_data['password']
            print(uname)
            print(pas)
            user = authenticate(username=uname, password=pas)

            if user is not None:
                login(request, user)

            return redirect("/")
    else:
        a = AuthenticationForm()

    context = {
        'a': a
    }
    return render(request, 'authenticationapp/login.html', context)


def profile_page(request):
    return render(request, 'authenticationapp/profile.html')


def logouthandle(request):
    logout(request)
    return redirect("/")
