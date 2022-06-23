import json
from urllib import response
from django.test import TestCase
from requests import request
from rest_framework import status
from django.contrib.auth.models import User as Admin
from django.contrib.auth.models import AbstractUser, UserManager
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from mixer.backend.django import mixer
from .views import ProjectModelViewSet
from .models import TODO, User


class TestProjectModelViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUsersCustomViewSet(TestCase):
    def test_get_detail(self):
        user = mixer.blend(User)
        client = APIClient()
        response = client.get(f'/api/custom_users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# class User(AbstractUser, UserManager):
#     pass

class TestTODOModelViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # def test_edit(self):
    #     todo = mixer.blend(TODO)
    #     admin = User.create_superuser('admin', 'admin@admin.com', 'admin123456')
    #     self.client.login(username='admin', password='admin364315')
    #     response = self.client.put(f'/api/notes/{todo.id}/', {'text': 'Good job', 'user': todo.user.id})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     todo = TODO.objects.get(id=todo.id)
    #     self.assertEqual(TODO.text, 'Good job')