from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def categories(request):
    all_categories = models.Category.objects.all()
    return {'all_categories': all_categories}