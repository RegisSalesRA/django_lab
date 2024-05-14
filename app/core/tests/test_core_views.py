from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Category, Tag, Task
from mocks.api_routes_mock import ApiRouteMocks as routes
from mocks.data_mock import DataMocks as dataJsonMock


class TaskAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_tasks(self):
        res = self.client.get(routes.url_api_get_tasks())
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_task_detail(self):
        tag = Tag.objects.create(name="Tag_1")
        category = Category.objects.create(name="Category_1")
        task = Task.objects.create(name="Task_1", category=category)
        task.tags.add(tag)

        res = self.client.get(routes.url_api_get_task(task.id))
    
        self.assertEqual(res.data['name'], task.name)
