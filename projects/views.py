from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from projects.serializers import *
from projects.models import *
from authentication.models import * 
from rest_framework.permissions import IsAuthenticated
from .permissions import *
 
class ProjectView(ModelViewSet):
    
    serializer_class = ProjectSerializer
    """ ProjectAuthentication class check if user is contributor of the project object before access it with GET method """
    permission_classes = [IsAuthenticated, ProjectAuthentication]
    
    def get_queryset(self):
        """ Get Project objects filter only for project contributors """
        return Project.objects.filter(contributors=self.request.user)
    
    def partial_update(self, request, *args, **kwargs):
        """ PATCH method overright to permit contributors project adding """
        instance = self.get_object()
        if 'contributors' in request.data:
            instance.contributors.add(request.data['contributors'])
            instance.save()
            serializer = ProjectSerializer(instance)
            return Response(serializer.data)
        else:
            """ return usual PATCH method for other model parameters """
            return super().partial_update(request, *args, **kwargs)


class IssueView(ModelViewSet):
    
    serializer_class = IssueSerializer
    """ IssueAuthentication class check if user is contributor of the project object before posting an issue associated to it with POST method
    Same verification is made to get any issue object. It also check if user is object author for method PATCH, DELETE OR PUT method """
    permission_classes = [IsAuthenticated, IssueAuthentication]

    def create(self, request, *args, **kwargs):
        """ POST method overright get user for assigned_to model parameter and assign it with project_id and author to model parameters"""
        serializer = self.serializer_class(data=request.data)
        assigned_to = User.objects.get(id=request.data['assigned_to'])
        if serializer.is_valid():
            serializer.save(project_id=request.data['project_id'], assigned_to=assigned_to, author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def partial_update(self, request, *args, **kwargs):
        """ PATCH method overright to allow user to change assigned_to model parameter """
        instance = self.get_object()
        
        if 'assigned_to' in request.data:
            instance.assigned_to = User.objects.get(id=request.data['assigned_to'])
            instance.save()
            instance.project.contributors.add(request.data['assigned_to'])
            instance.project.save()
            serializer = IssueSerializer(instance)
            return Response(serializer.data)
        else:
            """ return usual PATCH method for other parameters """
            return super().partial_update(request, *args, **kwargs)
    
    def get_queryset(self):
        """ Get Comment objects filter by Project queryset which has already been filtered """
        projects = ProjectView.get_queryset(self)
        return Issue.objects.filter(project__in=projects)

class CommentView(ModelViewSet):
    
    serializer_class = CommentSerializer
    """ CommentAuthentication check if user is a project contributor for the issue associated to the comment model for POST method
    Same verification is made to get any issue object. It also check if user is object author for PATCH, DELETE OR PUT method """
    permission_classes = [IsAuthenticated, CommentAuthentication]

    def create(self, request, *args, **kwargs):
        """ POST method overright to get issue_id and author model parameters """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(issue_id=request.data["issue_id"], author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get_queryset(self):
        """ Get Comment objects filter by Issue queryset which has already been filtered """
        issues = IssueView.get_queryset(self)
        return Comment.objects.filter(issue__in=issues)
