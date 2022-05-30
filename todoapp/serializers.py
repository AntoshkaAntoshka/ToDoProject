from rest_framework import serializers
from .models import Project, TODO
from userworkapp.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TODOSerializer(serializers.HyperlinkedModelSerializer):
    # project = ProjectSerializer()
    # user = UserSerializer()
    class Meta:
        model = TODO
        fields = '__all__'