from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "id",
        "nom",
        "mail",
        "contact",
        "type_compte",
        "adresse",
    ]
    
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("nom",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("nom",)}),)
    

admin.site.register(CustomUser, CustomUserAdmin) 
    
