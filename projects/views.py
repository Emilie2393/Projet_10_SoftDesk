from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from projects.serializers import *
from projects.models import *
from rest_framework.permissions import IsAuthenticated
from .permissions import *
 
class ProjectView(ModelViewSet):
    
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailsSerializer
    permission_classes = [IsAuthenticated, AuthorAuthentication]

    def post(self, request):
        self.detail_serializer_class.data == request.data
        self.detail_serializer_class.save()
        return Response(self.detail_serializer_class.data)
    
    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
    # Si l'action demandée est retrieve nous retournons le serializer de détail
        if self.action == 'list':
            return self.serializer_class
        elif self.action =='retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

class IssueView(ModelViewSet):
    
    serializer_class = IssueSerializer
    detail_serializer_class = IssueDetailsSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        self.detail_serializer_class.data == request.data
        self.detail_serializer_class.save()
        return Response(self.serializer_class.data)
    
    def get_queryset(self):
        return Issue.objects.all()
    
    def get_serializer_class(self):
    # Si l'action demandée est retrieve nous retournons le serializer de détail
        if self.action == 'list':
            return self.serializer_class
        elif self.action =='retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    
