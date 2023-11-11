from django.shortcuts import render,HttpResponse

# Create your views here.


def set(request):
    request.session['name'] = 'mohit'
    request.session.set_expiry(600)
    return render(request,'set.html')


def get(request):

    if 'name' in request.session:
        session_data = request.session['name']
        session_data = request.session.get('name',default='guest')
        request.session.modified = True
        return render(request,'get.html',{'session':session_data})
    else:
        return HttpResponse("Your Session Has Expired....")


def delete(request):

    if 'name' in request.session:
        del request.session['name']

        return render(request,'del.html')
    

def flush(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'del.html')