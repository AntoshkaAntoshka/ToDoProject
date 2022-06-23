from urllib import response
from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from userworkapp.models import User
from .serializers import TODOSerializerBase, UserSerializer, ProjectSerializer, TODOSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .filters import ProjectFilterName, TODOFilter
from django_filters import rest_framework as filters

class AllLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ProjectFilterName

class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    pagination_class = TODOLimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = TODOFilter
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TODOSerializer
        return TODOSerializerBase


class UsersModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = AllLimitOffsetPagination
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class UsersCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = AllLimitOffsetPagination
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

