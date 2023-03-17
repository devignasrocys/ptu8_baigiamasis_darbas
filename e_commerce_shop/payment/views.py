import json
from django.shortcuts import render
from . import models
from cart.cart import Cart
from django.http import JsonResponse

# Create your views here.
def checkout(request):
    if request.user.is_authenticated:
        try:
            shipping_address = models.ShippingAddress.objects.get(user=request.user.id)
            context = {'shipping': shipping_address}
            return render(request, 'payment/checkout.html', context=context)
        except:
            return render(request, 'payment/checkout.html')
    else:
        return render(request, 'payment/checkout.html')
    
def complete_order(request):
    cart = Cart(request)
    order_success = False
    if request.method == 'POST':
        data = json.loads(request.body)
        if request.user.is_authenticated:
            shipping_address = models.ShippingAddress.objects.get(user=request.user.id)
            order = models.Order.objects.create(
            full_name=data['name'],
            email=data['email'],
            amount_paid=cart.get_total(),
            user=request.user, 
            shipping_address=shipping_address)
            for item in cart:
                models.OrderItem.objects.create(order=order, product=item['product'], quantity=item['qty'], user=request.user) 
            cart.clear()
        else:
            shipping_address = models.ShippingAddress.objects.create(
                full_name=data['name'],
                email=data['email'],
                address1=data['address1'],
                address2=data['address2'],
                state=data['state'],
                zipcode=data['zipcode']
            )
            order = models.Order.objects.create(
            full_name=data['name'],
            email=data['email'],
            amount_paid=cart.get_total(),
            shipping_address=shipping_address)
            for item in cart:
                models.OrderItem.objects.create(order=order, product=item['product'], quantity=item['qty']) 
            cart.clear()
        order_success = True       
        response = JsonResponse({'order_success': order_success,})
        return response

def payment_success(request):
    return render(request, 'payment/payment-success.html')

def payment_failed(request):
    return render(request, 'payment/payment-failed.html')