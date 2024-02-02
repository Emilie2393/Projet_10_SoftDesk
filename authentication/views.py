from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from authentication.serializers import *
from authentication.models import *

 
class UserRegisterView(ModelViewSet):
    
    serializer_class = UserSerializer

    def post(self, request):
        self.serializer_class.data == request.data
        self.serializer_class.save()
        return Response(self.serializer_class.data)

    def get_queryset(self):
        return User.objects.all()

"""class LoginView(ModelViewSet):

    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()

        if not user.check_password(password):
            raise AuthenticationFailed('wrong password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        return Response({'jwt': token})"""

