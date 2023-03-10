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

    if request.POST.get('action') == 'post':
        print(request)
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_quantity)
        cart_quantity = cart.__len__()
        response = JsonResponse({'quantity': cart_quantity})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass