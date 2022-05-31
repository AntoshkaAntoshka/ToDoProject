from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from userworkapp.models import User
from .serializers import UserSerializer, ProjectSerializer, TODOSerializer
from rest_framework.pagination import LimitOffsetPagination


class AllLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

class UsersModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = AllLimitOffsetPagination

