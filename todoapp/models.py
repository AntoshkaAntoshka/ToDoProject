from django.db import models
from userworkapp.models import User

class Project(models.Model):
    project_title = models.CharField('Title', max_length=64)
    link_to_repo = models.TextField('Link', max_length=200, blank=True)
    project_authors = models.ManyToManyField(User)

    def __str__(self):
        return self.project_title

class TODO(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField('Description', max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, models.PROTECT)

