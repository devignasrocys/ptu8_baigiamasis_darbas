# Generated by Django 4.1.7 on 2023-03-22 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_shippingaddress_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='city',
        ),
    ]