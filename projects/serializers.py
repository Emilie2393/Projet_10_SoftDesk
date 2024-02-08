from rest_framework import serializers
from projects.models import *
from authentication.serializers import *
    

class ProjectDetailsSerializer(serializers.ModelSerializer):

    contributors = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['name', 'author', 'contributors', 'description', 'type']
    
    def create(self, validated_data):
        contributors = validated_data.pop("contributors", [])
        user = self.context["request"].user
        validated_data["author"] = user
        instance = Project.objects.create(**validated_data)
        instance.contributors.add(user)
        return instance
    
    def get_contributors(self, instance):
        queryset = instance.contributors.all()
        serializer = UserSerializer(queryset, many=True)
        return serializer.data
    
    def get_author(self, instance):
        queryset = instance.author
        serializer = UserSerializer(queryset)
        return serializer.data

class ProjectSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['name', 'author', 'type']
        # hide password into the get view
    
    def get_author(self, instance):
        queryset = instance.author
        serializer = UserDetailsSerializer(queryset)
        return serializer.data

class IssueDetailsSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()
    assigned_to = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = ['project', 'name', 'author', 'assigned_to', 'description', 'priority', 'tag', 'status']
    
    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["author"] = user
        instance = Issue.objects.create(**validated_data)
        project = Project.objects.get(id=instance.project.id)
        project.contributors.add(user)
        project.contributors.add(instance.assigned_to.id)
        project.save()
        return instance
    
    def get_author(self, instance):
        queryset = instance.author
        serializer = UserSerializer(queryset)
        return serializer.data['username']
    
    def get_assigned_to(self, instance):
        queryset = instance.assigned_to
        serializer = UserSerializer(queryset)
        return serializer.data['username']

class IssueSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()
    class Meta:
        model = Issue
        fields = ['project', 'name', 'author', 'priority', 'status']
    
    def get_author(self, instance):
        queryset = instance.author
        serializer = UserSerializer(queryset)
        return serializer.data['username']


        
