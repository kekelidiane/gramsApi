from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.EmailField(label='Email', max_length=254)
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('nom', 'email', 'contact', 'date_naissance', 'adresse', 'type_compte')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('nom', 'email', 'contact', 'date_naissance', 'adresse', 'type_compte', 'is_staff', 'is_superuser')
