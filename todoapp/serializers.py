from rest_framework import serializers
from .models import Project, TODO
from userworkapp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TODOSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
        

class TODOSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    user = UserSerializer()
    class Meta:
        model = TODO
        fields = '__all__'