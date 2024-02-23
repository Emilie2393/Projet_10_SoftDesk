from rest_framework.permissions import BasePermission
from projects.models import *

 
class ProjectAuthentication(BasePermission):
    """ ProjectAuthentication class check if user is contributor of the
    project object before access it with GET method """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
 
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return bool(request.user in obj.contributors.all())
        return bool(obj.author == request.user)

class IssueAuthentication(BasePermission):
    """ IssueAuthentication class check if user is contributor of the project
    object before posting an issue associated to it with POST method
    Same verification is made to get any issue object. It also check if user
    is object author for method PATCH, DELETE OR PUT method """

    def has_permission(self, request, view):
        if request.method in ['POST']:
            project = Project.objects.get(id=request.data['project_id'])
            return bool(request.user in project.contributors.all())
        return bool(request.user and request.user.is_authenticated)
 
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return bool(request.user in obj.project.contributors.all())
        """if request.method in ['PATCH', 'DELETE', 'PUT']:"""
        return bool(obj.author == request.user)

class CommentAuthentication(BasePermission):
    """ CommentAuthentication check if user is a project contributor for the issue 
    associated to the comment model for POST method. Same verification is made to get
    any issue object. It also check if user is object author for PATCH, DELETE OR
    PUT method """

    def has_permission(self, request, view):
        if request.method in ['POST']:
            issue = Issue.objects.get(id=request.data['issue_id'])
            return bool(request.user in issue.project.contributors.all())
        return bool(request.user and request.user.is_authenticated)
 
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return bool(request.user in obj.issue.project.contributors.all())
        return bool(obj.author == request.user)
        
        

