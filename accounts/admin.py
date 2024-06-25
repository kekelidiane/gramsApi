from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        'nom',
        'email',
        'is_staff',
        'is_superuser'
    )
    list_filter = (
        'is_staff',
        'is_superuser', 
        'is_active', 
        'type_compte'
    )
    fieldsets = (
        (None, {'fields': ('nom', 'email', 'password', 'contact')}),
        ('Personal Info', {'fields': ('date_naissance', 'adresse', 'type_compte')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nom', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active')}
        ),
    )
    search_fields = ('email', 'nom')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
