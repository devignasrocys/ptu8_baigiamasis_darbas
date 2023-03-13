from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from . import models

# Create your views here.
def home(request):
    all_products = models.Product.objects.all()
    context = {'all_products': all_products}
    query = request.GET.get('search')
    if query:
        all_products = all_products.filter(
            Q(title__istartswith=query)
        )
        context = {'all_products': all_products}
        return render(request, 'core/search-page.html', context)
    print(query)
    return render(request, 'core/home.html', context)

def categories(request):
    all_categories = models.Category.objects.all()
    return {'all_categories': all_categories}

def product_info(request, slug):
    product = get_object_or_404(models.Product, slug=slug)
    context = {'product': product}
    return render(request, 'core/product-info.html', context)

