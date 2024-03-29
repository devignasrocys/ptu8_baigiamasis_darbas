# Generated by Django 4.1.7 on 2023-03-16 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('shipping_address', models.TextField(max_length=10000)),
                ('amount_pad', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Shipping Address',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='payment.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='core.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
