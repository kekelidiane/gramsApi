from rest_framework import permissions
from accounts.models import CustomUser


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.user.is_authenticated(): # Read permissions
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS: 
            return True
        
        return obj.author == request.user # Write permissions