from django_filters import rest_framework as filters
from .models import Project

class ProjectFilterName(filters.FilterSet):
    name = filters.CharFilter(field_name='project_title', lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['project_title']
