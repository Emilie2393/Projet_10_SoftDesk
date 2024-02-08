from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from authentication.serializers import *
from authentication.models import *


class UserRegisterView(ModelViewSet):
    
    serializer_class = UserDetailsSerializer

    def post(self, request):
        self.serializer_class.data == request.data
        self.serializer_class.save()
        return Response(self.serializer_class.data)

    def get_queryset(self):
        return User.objects.all()


