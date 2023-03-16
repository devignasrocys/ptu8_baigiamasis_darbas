from django.shortcuts import render
from . import models

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
    pass