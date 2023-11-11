from django.shortcuts import render

# Create your views here.


def setCookie(request):
    response = render(request,'setCookie.html')
    response.set_cookie('name','mohit',max_age=5)
    print(response)
    return response

def getCookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name','guest')
    return render(request,'getCookie.html',{'name':name})

def delCookie(request):
    response = render(request,'deleteCookie.html')
    response.delete_cookie('name')
    return response