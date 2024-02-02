from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from projects.serializers import ProjectSerializer
from projects.models import *
from rest_framework.permissions import IsAuthenticated
 
class ProjectCreationView(ModelViewSet):
    
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        self.serializer_class.data == request.data
        self.serializer_class.save()
        return Response(self.serializer_class.data)
    
    def get_queryset(self):
        return Project.objects.all()