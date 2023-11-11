from django.shortcuts import render,HttpResponse
from .models import student,form_data
# from .forms import student_forms
from .forms import profile_form

# Create your views here.


# def index(request):
#     data = student.objects.all()

#     if request.method == "POST":
#         form_data = student_forms(request.POST)
#         if form_data.is_valid():
#             form_data.save()
    
#     else:

#      form_data = student_forms()
    
#     print(form_data)
#     context = {

#         'd':data,
#         'f':form_data
#     }
#     return render(request,'index.html',context)




# def my_form(request):

#     if request.method =="POST":
#         a = myform(request.POST)

#         if a.is_valid():

#             n = request.POST['name']
#             e = request.POST['email']
#             a = request.POST['address']

#             form_data(name=n,email=e,address=a).save()

#             return HttpResponse("Your data saved !!!")
        
#         else:

#             return HttpResponse("Data Not Saved !!!")
           
       
    
#     else:

#       a = myform()
#       print(a)
    
#     context = {

#         'a':a
#     }

#     return render(request,'forms.html',context)



def profileform(request):

    if request.method == "POST":

        a = profile_form(request.POST,request.FILES):

        if a.is_valid():
            

        
    a = profile_form()
    context = {
        'a':a
    }
    return render(request,'new_form.html',context)




     
  




