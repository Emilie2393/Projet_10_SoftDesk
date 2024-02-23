from rest_framework.permissions import BasePermission

 
class UserAuthentication(BasePermission):
    """ ProjectAuthentication class check if user is contributor of the
    project object before access it with GET method """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
 
    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user)