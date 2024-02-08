from rest_framework.permissions import BasePermission
 
class AuthorAuthentication(BasePermission):
 
    def has_object_permission(self, request, view, obj):
    # Ne donnons l’accès qu’aux utilisateurs administrateurs authentifiés
        if request.method in ['PUT']:
            if obj.author == request.user:
                return True
            else:
                return False
        else:
            return True
