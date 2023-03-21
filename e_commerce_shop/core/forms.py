from django import forms
from . import models


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = models.ProductReview
        fields = ('review', 'rating',)
        labels = {
            'review': 'You can leave a review!',
            'rating': 'Rate this product'
        }