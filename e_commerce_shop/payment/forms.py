from django.contrib.auth import get_user_model
from django import forms
from . import models

User = get_user_model()

class ShippingForm(forms.ModelForm):
    class Meta:
        model = models.ShippingAddress
        fields = ('full_name', 'email', 'city', 'address1', 'address2', 'state', 'zipcode')