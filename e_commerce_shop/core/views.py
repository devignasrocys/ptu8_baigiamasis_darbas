from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . import models
from . import forms
from payment import models as payment_models


# Create your views here.
def home(request):
    products = models.Product.objects.all()
    top_products = []
    for product in products:
       if product.product_reviews.all():
           if sum(product.product_reviews.all().values_list('rating', flat=True)) / len(product.product_reviews.all()) >= 4:
               top_products.append(product)
    context = {'all_products': top_products}
    return render(request, 'core/home.html', context)

def categories(request):
    all_categories = models.Category.objects.all()
    context = {'all_categories': all_categories}
    return context

def list_category(request, category_slug=None):
    category = get_object_or_404(models.Category, slug=category_slug)
    products = models.Product.objects.filter(category=category)
    context = {'category': category, 'products': products}
    query = request.GET.get('search')
    if query:
        products = products.filter(
            Q(title__istartswith=query)
        )
        context = {'category': category, 'all_products': products}
        return render(request, 'core/search-page.html', context)
    return render(request, 'core/list-category.html', context)


def product_info(request, slug):
    product = get_object_or_404(models.Product, slug=slug)
    reviews = models.ProductReview.objects.filter(product=product)
    context = {'product': product, 'stock_quantity': range(1, product.stock + 1), 'form': forms.ProductReviewForm(), 'reviews': reviews}
    if request.user.is_authenticated:
        products_bought_by_user = payment_models.OrderItem.objects.filter(user=request.user, product=product)
        if products_bought_by_user:
            product_already_bought = True
        else:
            product_already_bought = False
        if request.method == 'POST':
            form = forms.ProductReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.product = product
                review.save()
                return redirect('product-info', slug=slug)
        if products_bought_by_user:
            context['product_already_bought'] = product_already_bought
    return render(request, 'core/product-info.html', context)


