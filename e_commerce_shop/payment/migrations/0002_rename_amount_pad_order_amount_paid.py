# Generated by Django 4.1.7 on 2023-03-16 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='amount_pad',
            new_name='amount_paid',
        ),
    ]
