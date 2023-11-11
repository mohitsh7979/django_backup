from django.shortcuts import render,HttpResponse,redirect
from .forms import student_forms,s_form,resgister_form
from .models import student_models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout


# Create your views here.


def index(request):

    # if request.method == "POST":
    #   form = UserCreationForm(request.POST)
    #   print(form)

    #   if form.is_valid():
    #       form.save()
    #       return HttpResponse('Account created !!!')
    
    form  = resgister_form()
    
    return render(request,'index.html',{'form':form})

def form(request):

    if request.method == "POST":
        form_data = student_forms(request.POST,request.FILES)
        print(form_data)

        if form_data.is_valid():
            name  = form_data.cleaned_data['name']
            email = form_data.cleaned_data['email']
            mobile_no = form_data.cleaned_data['mobile_no']
            skill = form_data.cleaned_data['skills']
            image = form_data.cleaned_data['image']

            student_models(name=name,email=email,mobile_no=mobile_no,skills=skill,image=image).save()

            return HttpResponse('Data Saved !!')

    form_data = student_forms()
    context = {
        'form_data':form_data
    }
    return render(request,'contact.html',context)



def get_data(request):
    
    data = student_models.objects.all()
    context = {

        'data':data,
        
    }
    return render(request,'content.html',context)


def index1(request):
    context = {'form':student_forms()}
    return render(request,'index1.html',context)


# def create_contact(request):

#     if request.method == "POST":
        
#         data  = s_form(request.POST)
        
#         if data.is_valid():

#             name = data.cleaned_data['name']
#             m = data.cleaned_data['mobile_no']
#             print(name,m)

#     return render(request,'my_form.html',{'form':s_form})




def create_account(request):

    if request.method == "POST":
        x = resgister_form(request.POST)

        if x.is_valid():
            x.save()
            return HttpResponse('Data Saved !!')

    x = resgister_form()
    my_dict = {

        'x':x

    }

    return render(request,'auth_forms.html',my_dict)



def login_form(request):

    if request.method == "POST":
        x = AuthenticationForm(data = request.POST)
        print('>>>>x',x)
        if x.is_valid():
            uname = x.cleaned_data['username']
            passw = x.cleaned_data['password']
            user = authenticate(username = uname , password = passw)

            if user is not None:
                login(request,user)
                return redirect('/get/')
            
    x = AuthenticationForm()      
    context = {
        'x':x
    }

    return render(request,'login_form.html',context)


def get_out(request):
    logout(request)
    return redirect('/login/')


