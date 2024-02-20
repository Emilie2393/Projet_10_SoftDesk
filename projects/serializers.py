from rest_framework import serializers
from projects.models import *
from authentication.serializers import *
    

class ProjectSerializer(serializers.ModelSerializer):

    contributors = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'author', 'contributors', 'description', 'type']
    
    def create(self, validated_data):
        """ Replace contributor and author parameter by user """
        validated_data.pop("contributors", [])
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
        serializer = UserDetailsSerializer(queryset)
        return serializer.data


class IssueSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()
    assigned_to = serializers.SerializerMethodField()
    project_id = serializers.SerializerMethodField()


    class Meta:
        model = Issue
        fields = ['id', 'project_id', 'name', 'author', 'assigned_to', 'description', 'priority', 'tag', 'status']
    
    def create(self, validated_data):
        """ Create Issue instance and add user assigned_to to project contributors """
        instance = Issue.objects.create(**validated_data)
        project = Project.objects.get(id=instance.project.id)
        project.contributors.add(instance.assigned_to.id)
        project.save()
        return instance
    
    def get_author(self, instance):
        queryset = instance.author
        serializer = UserSerializer(queryset)
        return serializer.data
    
    def get_assigned_to(self, instance):
        queryset = instance.assigned_to
        serializer = UserSerializer(queryset)
        return serializer.data
    
    def get_project_id(self, instance):
        queryset = instance.project
        serializer = ProjectSerializer(queryset)
        return serializer.data['id']

class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()
    project_id = serializers.SerializerMethodField()
    issue_id = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['project_id', 'issue_id', 'author', 'description']
    
    """ These get methods are using others models serializer """
    def get_author(self, instance):
        queryset = instance.author
        serializer = UserSerializer(queryset)
        return serializer.data
    
    def get_project_id(self, instance):
        queryset = instance.issue.project
        serializer = ProjectSerializer(queryset)
        return serializer.data['id']

    def get_issue_id(self, instance):
        queryset = instance.issue
        serializer = IssueSerializer(queryset)
        return serializer.data['id']
    
        
