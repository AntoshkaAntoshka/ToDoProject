import graphene
from graphene_django import DjangoObjectType
from userworkapp.models import User
from todoapp.models import Project, TODO

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todo = graphene.List(TODOType)
    todo_by_id = graphene.Field(TODOType, id=graphene.Int(required=True))
    project_by_name = graphene.List(ProjectType, name=graphene.String(required=False))

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todo(root, info):
        return TODO.objects.all()

    def resolve_todo_by_id(self, info, id):
        try:
            return TODO.objects.get(id=id)
        except TODO.DoesNotExist:
            return None

    def resolve_project_by_name(self, info, name=None):
        projects = Project.objects.all()
        if name:
            projects = projects.filter(project_authors__first_name=name)
        return projects

schema = graphene.Schema(query=Query)