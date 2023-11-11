from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect
from .models import *
from authenticationapp.models import Customer

# Create your views here.


def product(request):
    featuredproduct = Product.objects.filter(catagory='f')
    latestproduct = Product.objects.filter(catagory='l')
    offerproduct = Product.objects.filter(catagory='o')
    context = {
        'featuredproduct': featuredproduct,
        'latestproduct': latestproduct,
        'offerproduct': offerproduct
    }

    return render(request, 'productapp/e-commerce.html', context)


def productview(request, id):
    a = Product.objects.get(id=id)
    context = {
        'a': a,
        'color': a.color.split(',') if a.color else []
    }
    return render(request, 'productapp/productview.html', context)


def addcart(request):
    if request.method == "POST":
        user = request.user
        product_id = request.POST['prod_id']
        prod = Product.objects.get(id=product_id)
        color = request.POST.get('color')
        cart = Cart(user=user, product=prod) #send color as well.
        cart.save()
    return redirect('/showcart')


def showcart(request):

    user = request.user
    showcart = Cart.objects.filter(user=user)
    print(showcart)
    context = {
        'showcart': showcart
    }

    amount = 0.0
    total_amount = 0.0
    tax = 70.0

    cart_product = [p for p in showcart if p.user == user]
    print("this is cart_product :", cart_product)
    if cart_product:
        print("if cart product :", cart_product)
        for p in cart_product:
            print("This is p :", p)

            print(p, 'ye only p hain')
            teampamount = p.product.price
            print('teampamount', teampamount)
            amount = amount+teampamount
            print('amount =', amount)
            total_amount = amount+tax
            print('This is total amoutn', total_amount)
            context = {
                'amount': amount,
                'total_amount': total_amount,
                'showcart': showcart
            }
        return render(request, 'productapp/cart.html', context)
    else:
        return render(request, 'productapp/emptycart.html', context)
    print(cart_product)

    return render(request, 'productapp/cart.html', context)


def checkout(request):
    user = request.user
    a = Cart.objects.filter(user=user)
    b = Customer.objects.filter(user=user)
    print(a)
    print(b)
    context = {
        'a': a,
        'b': b
    }

    return render(request, 'productapp/checkout.html', context)


def paymentdone(request):
    usr = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    print(customer)
    cart = Cart.objects.filter(user=usr)

    for c in cart:
        print(c)

        Orderplaced(user=usr, customer=customer,
                    product=c.product, quantity=c.quantity).save()

        c.delete()
    order_data = Orderplaced.objects.filter(user=usr)
    print(order_data)
    return render(request, 'productapp/orderdetails.html', {'order_data': order_data})


def header(request):
    return render(request, 'productapp/headerandfooter.html')


def men(request, data=None):
    if data == None:

        menproduct = Product.objects.filter(catagory='m')

    elif data == 'Below':
        menproduct = Product.objects.filter(catagory='m').filter(price__lt=500)

    elif data == 'above':
        menproduct = Product.objects.filter(catagory='m').filter(price__gt=500)

    elif data == 'shirt':
        menproduct = Product.objects.filter(catagory='m').filter(brand='s')

    elif data == 't-shirt':
        menproduct = Product.objects.filter(catagory='m').filter(brand='t')

    elif data == 'Jeans':
        menproduct = Product.objects.filter(catagory='m').filter(brand='j')

    elif data == 'Paint':
        menproduct = Product.objects.filter(catagory='m').filter(brand='p')

    context = {'menproduct': menproduct}
    return render(request, 'productapp/men.html', context)


def women(request, data=None):

    if data == None:

        womenproduct = Product.objects.filter(catagory='w')

    elif data == 'Below':
        womenproduct = Product.objects.filter(
            catagory='w').filter(price__lt=500)

    elif data == 'above':
        womenproduct = Product.objects.filter(
            catagory='w').filter(price__gt=500)

    elif data == 'shirt':
        womenproduct = Product.objects.filter(catagory='w').filter(brand='s')

    elif data == 'toper':
        womenproduct = Product.objects.filter(catagory='w').filter(brand='T')

    elif data == 'Jeans':
        womenproduct = Product.objects.filter(catagory='w').filter(brand='j')

    # elif data == 'Paint':
    #     womenproduct = Product.objects.filter(catagory='m').filter(brand='p')

    context = {'womenproduct': womenproduct}
    return render(request, 'productapp/women.html', context)


def kids(request, data=None):

    if data == None:

        kidsproduct = Product.objects.filter(catagory='k')

    elif data == 'Below':
        kidsproduct = Product.objects.filter(
            catagory='k').filter(price__lt=500)

    elif data == 'above':
        kidsproduct = Product.objects.filter(
            catagory='k').filter(price__gt=500)

    elif data == 'shirt':
        kidsproduct = Product.objects.filter(catagory='k').filter(brand='s')

    elif data == 'toper':
        kidsproduct = Product.objects.filter(catagory='k').filter(brand='T')

    elif data == 'Jeans':
        kidsproduct = Product.objects.filter(catagory='k').filter(brand='j')
    return render(
        request,
        'productapp/kids.html',
        {'kidsproduct': kidsproduct}
    )


def productdelete(request, id):
    # product=Cart.objects.all()
    # print(product)
    # for i in product:
    #     print(i.id)
    product = Cart.objects.get(id=id)
    print(product)
    product.delete()

    return redirect("/showcart/")
    # return render(request,'productapp/kids.html')


def orderdetails(request):
    order_data = Orderplaced.objects.filter(user=request.user)
    print(order_data)
    return render(request, 'productapp/orderdetails.html', {'order_data': order_data})
