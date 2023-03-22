from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])


class Product(models.Model):

    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField(max_length=1500, blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    image4 = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
    

class ProductReview(models.Model):
    RATING_CHOICES = (
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField(max_length=1500, blank=True)
    rating = models.IntegerField(default=0, choices=RATING_CHOICES,)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review

    class Meta:
        verbose_name_plural = 'product reviews'