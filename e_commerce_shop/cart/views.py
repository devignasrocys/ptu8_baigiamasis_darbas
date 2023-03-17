import json
from django.shortcuts import render
from .cart import Cart
from core.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse

# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    
    return render(request, 'cart/cart-summary.html', {'cart': cart})

def cart_add(request):
    cart = Cart(request)

    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = int(data['product_id'])
        product_quantity = int(data['product_quantity'])
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_quantity)
        cart_quantity = cart.__len__()
        response = JsonResponse({'quantity': cart_quantity,})
        return response
    
def cart_delete(request):
    cart = Cart(request)

    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = int(data['product_id'])
        cart.delete(product_id=product_id,)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total()
        response = JsonResponse({'quantity': cart_quantity, 'total': cart_total})
        return response



def cart_update(request):
    cart = Cart(request)

    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        product_id = int(data['product_id'])
        product_quantity = int(data['product_quantity'])
        cart.update(product_id=product_id,product_quantity=product_quantity)
        cart_quantity = cart.__len__()
        response = JsonResponse({'quantity': cart_quantity,})
        return response