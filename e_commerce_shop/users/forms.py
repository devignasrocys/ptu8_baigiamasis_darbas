from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')