from django.shortcuts import render

# Create your views here.


def set(request):
    request.session['name'] = 'mohit'
    return render(request,'set.html')


def get(request):
    session_data = request.session['name']
    session_data = request.session.get('name',default='guest')
    key = request.session.keys()
    value = request.session.values()
    item = request.session.items()
    age = request.session.setdefault('age',26)
    print(session_data)
    return render(request,'get.html',{'session':session_data,'key':key,'item':item,'age':age})


def delete(request):

    if 'name' in request.session:
        del request.session['name']

        return render(request,'del.html')
    

def flush(request):
    request.session.flush()
    return render(request,'del.html')