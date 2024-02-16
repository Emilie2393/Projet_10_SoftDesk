from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from projects.serializers import *
from projects.models import *
from authentication.models import * 
from rest_framework.permissions import IsAuthenticated
from .permissions import *
 
class ProjectView(ModelViewSet):
    
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, AuthorAuthentication]
    
    def get_queryset(self):
        return Project.objects.filter(contributors=self.request.user)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'contributors' in request.data:
            instance.contributors.add(request.data['contributors'])
            instance.save()
            serializer = ProjectSerializer(instance)
            return Response(serializer.data)
        else:
            return super().partial_update(request, *args, **kwargs)


class IssueView(ModelViewSet):
    
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, AuthorAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        assigned_to = User.objects.get(id=request.data['assigned_to'])
        if serializer.is_valid():
            serializer.save(project_id=request.data['project_id'], assigned_to=assigned_to, author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'assigned_to' in request.data:
            instance.assigned_to = User.objects.get(id=request.data['assigned_to'])
            instance.save()
            serializer = IssueSerializer(instance)
            return Response(serializer.data)
        else:
            return super().partial_update(request, *args, **kwargs)
    
    def get_queryset(self):
        projects = ProjectView.get_queryset(self)
        print(projects)
        return Issue.objects.filter(project__in=projects)

class CommentView(ModelViewSet):
    
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, AuthorAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(issue_id=request.data["issue_id"], author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get_queryset(self):
        issues = IssueView.get_queryset(self)
        return Comment.objects.filter(issue__in=issues)
