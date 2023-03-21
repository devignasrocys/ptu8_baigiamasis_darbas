from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . import models
from . import forms


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
    return render(request, 'core/home.html', context)

def categories(request):
    all_categories = models.Category.objects.all()
    return {'all_categories': all_categories}

def list_category(request, category_slug=None):
    category = get_object_or_404(models.Category, slug=category_slug)
    products = models.Product.objects.filter(category=category)
    print(products)
    return render(request, 'core/list-category.html', {'category': category, 'products': products})


def product_info(request, slug):
    product = get_object_or_404(models.Product, slug=slug)
    reviews = models.ProductReview.objects.filter(product=product)
    if request.method == 'POST':
        form = forms.ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product-info', slug=slug)
    context = {'product': product, 'form': forms.ProductReviewForm(), 'reviews': reviews}
    return render(request, 'core/product-info.html', context=context)


