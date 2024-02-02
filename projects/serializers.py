from rest_framework import serializers
from projects.models import *
from authentication.serializers import *
    

class ProjectSerializer(serializers.ModelSerializer):

    contributors = UserSerializer

    class Meta:
        model = Project
        fields = '__all__'
        # hide password into the get view
    
    """def create(self, validated_data):
        print(validated_data)
        user = self.context['request.user']
        password = validated_data.pop('password', None)"""
