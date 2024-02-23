from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from authentication.serializers import *
from authentication.models import *
from .permissions import * 


class UserRegisterView(ModelViewSet):
    
    serializer_class = UserDetailsSerializer
    short_serializer_class = UserSerializer
    permission_classes = [UserAuthentication]

    def post(self, request):
        self.serializer_class.data == request.data
        self.serializer_class.save()
        return Response(self.serializer_class.data)

    def get_queryset(self):
        return User.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return self.short_serializer_class
        return super().get_serializer_class()


