from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse,redirect,render
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required



def Create_Account(request):
    try:
        if request.method == "POST":
            uname = request.POST.get('username')
            email = request.POST.get('email')
            passw = request.POST.get('password')
            print(uname,email,passw)
        
        try:

            if User.objects.filter(username=uname).first():
                messages.success(request,'username is taken')

            if User.objects.filter(email=email).first():
                messages.success(request,'email is taken')
            
            else:
                user = User(username=uname,email=email)
                user.set_password(passw)
                user.save()
                messages.success(request,'Account created !!')


        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
  
    return render(request,'auth_app/create_account.html')


def login_handle(request):


    try:

        if request.method == "POST":
            username = request.POST.get('username')
            password =request.POST.get('password')
            print(username,password)
           
            if not username or not password:
                messages.success(request,'Boths fields are required !')

            user_obj = User.objects.filter(username=username).first()
            user = authenticate(username=username,password=password)

            if user_obj is None:
                messages.success(request,'User Not found !')
            print(user_obj)

            if user is not None:
                login(request,user)
                return redirect('/home/')
            
            if user is None:
                messages.success(request,'Wrong Password !!')

        
    except Exception as e:
        print(e)

    return render(request,'auth_app/Login.html')


@login_required(login_url='/')
def logouthandle(request):

    try:

        logout(request)
    
    except Exception as e:
        print(e)

    return redirect("/")
    
