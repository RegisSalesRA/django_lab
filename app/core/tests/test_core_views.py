from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Category, Tag, Task
from mocks.api_routes_mock import ApiRouteMocks as routes


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

    def test_get_task_404(self):
        res = self.client.get(routes.url_api_get_task(20))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_method_not_allowed(self):
        res = self.client.post(routes.url_api_get_task(24))
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
