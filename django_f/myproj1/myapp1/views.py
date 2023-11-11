from django.shortcuts import render,HttpResponse,redirect
from .models import contact_detail,todolist
from django.contrib import messages
from .forms import Toform
from .models import todolist

# Create your views here.



def index(request):
    if request.method == "POST":
        uemail = request.POST['email']
        udescription = request.POST['description']
        print(uemail,udescription)
        contact_detail(email=uemail,description=udescription).save()
        messages.success(request,'Data Successfully saved !!!!')
        
    return render(request,'Index.html')

def men(request):
    a = 10
    b = 20
    c = "addtion :" + str(a+b)

    context = {
        'c':c
    }
    return render(request,'men.html',context)

def women(request):
    return render(request,'women.html')


def todo(request):
    if request.method == "POST":
        a = Toform(request.POST)
        if a.is_valid():
            a.save()
            return redirect('/to/')
        
    a = Toform()
    data = todolist.objects.all()
    return render(request,'to_do_list.html',{'a':a,'data':data})

def todo_update(request,id):
    if request.method == "POST":
        x = todolist.objects.get(id=id)
        a = Toform(request.POST,instance=x)
        if a.is_valid():
            a.save()
            return redirect('/to/')
        
    x = todolist.objects.get(id=id)
    a = Toform(instance=x)
    return render(request,'to_do_list.html',{'a':a})

    