
# from authentication.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from authentication.models import *

# User = get_user_model()

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'age', 'is_active', 'can_be_contacted', 'can_data_be_shared']
        # hide password into the get view
        extra_kwargs = {'password': {'write_only': True}}
    
    # between view and model creation
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        print(instance.age)
        # Adding the below line made it work for me.
        instance.is_active = True
        if password is not None:
            # Set password does the hash, so you don't need to call make_password 
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
