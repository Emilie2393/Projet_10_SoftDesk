from rest_framework.permissions import BasePermission
from projects.models import *

 
class ProjectAuthentication(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
 
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return bool(request.user in obj.contributors.all())
        return bool(obj.author == request.user)

class IssueAuthentication(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['POST']:
            project = Project.objects.get(id=request.data['project_id'])
            return bool(request.user in project.contributors.all())
        return bool(request.user and request.user.is_authenticated)
 
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return bool(request.user in obj.project.contributors.all())
        if request.method in ['PATCH', 'DELETE', 'PUT']:
            return bool(obj.author == request.user)

class CommentAuthentication(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['POST']:
            issue = Issue.objects.get(id=request.data['issue_id'])
            return bool(request.user in issue.project.contributors.all())
        return bool(request.user and request.user.is_authenticated)
 
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return bool(request.user in obj.issue.project.contributors.all())
        if request.method in ['PATCH', 'DELETE', 'PUT']:
            return bool(obj.author == request.user)
        
        

