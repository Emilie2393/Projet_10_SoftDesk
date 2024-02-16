from rest_framework.permissions import BasePermission
from projects.models import *

 
class AuthorAuthentication(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
 
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            if obj.author == request.user:
                return True
            else:
                return False
        else:
            return True
        
        

