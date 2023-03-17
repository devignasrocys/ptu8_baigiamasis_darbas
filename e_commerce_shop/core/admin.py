from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'brand', 'price',]
    prepopulated_fields = {'slug': ('title',)}

# admin.site.register(models.Category)
# admin.site.register(models.Product)
