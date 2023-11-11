from django.shortcuts import render,HttpResponse
from .forms import register_form
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def auth(request):

    if request.method == "POST":

        data = register_form(request.POST)

        if data.is_valid():
            data.save()
            return HttpResponse('data Saved !!')

    data = register_form()

    return render(request,'index.html',{'data':data})
