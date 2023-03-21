from django import forms
from . import models


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = models.ProductReview
        fields = ('review', 'rating',)