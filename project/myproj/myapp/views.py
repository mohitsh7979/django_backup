from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from myapp.forms import resetform
from django.contrib.auth.models import User
from .helpers import send_forget_password_mail
from django.contrib import messages
from .models import Profile,pic
from django.http import JsonResponse


# Create your views here.


def loginhandle(request):
       
    my_user = 0 
    if 'a' in request.POST:
        print('I am enter')
        a_value = request.POST['a']

        print(a_value)
        my_user = pic.objects.filter(user__username = a_value)
        # filtered_values = list(my_user.values_list('image', flat=True))
        image_urls = [image.image.url for image in my_user]
    
        return JsonResponse({'data':image_urls})



    if request.method == "POST":

        
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)

        user_obj = User.objects.filter(username = username).first()
        print("user_obj",user_obj)

        
        user = authenticate(username = username , password = password)

        if user_obj is None:

            messages.success(request,"User not found !!!")


        elif user is not None:

            login(request,user)

            return redirect('/project/table/')
        
        else:

            print("Wrong")
            messages.success(request,'password is not correct')

  
        
    return render(request,'myapp/login.html',{'b':my_user})


def ChangePassword(request , token):
    context = {}
    
    
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/')
            
            
            
        
        
    except Exception as e:
        print(e)
    return render(request , 'myapp/change-password.html' , context)

import uuid


def ForgetPassword(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        print(username)

        if not User.objects.filter(username=username).first():

            messages.success(request,'Not User Found with this username')

            return redirect('/forget-password/')
        
        user_obj = User.objects.get(username=username)
        print('user object',user_obj)
        token = str(uuid.uuid4())
        Profile(user = user_obj , forget_password_token = token ).save()
        # profile_obj = Profile.objects.get(user = user_obj)
        # print('Profile object',profile_obj)
        # profile_obj.forget_password_token = token
        # profile_obj.save()
        print("user_object email  token",user_obj.email , token)
        send_forget_password_mail(user_obj.email , token)
        messages.success(request,'An email is sent')
        return redirect('/forget-password/')
        
   


    
    return render(request,'myapp/reset.html')


def logouthandle(request):
    logout(request)
    return redirect("/")



    
        






            
    

  
