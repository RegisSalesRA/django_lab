from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from core.tests.helpers.task_helper_test import CategoryFactory, TagFactory, TaskFactory
from mocks.api_routes_mock import ApiRouteMocks as routes


class TaskAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_tasks(self):
        res = self.client.get(routes.url_api_get_tasks())
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_task_detail(self):
        task = TaskFactory(tags=[TagFactory()], category=CategoryFactory())
        res = self.client.get(routes.url_api_get_task(task.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], task.name)

    def test_get_task_404(self):
        res = self.client.get(routes.url_api_get_task(20))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_method_not_allowed(self):
        res = self.client.post(routes.url_api_get_task(24))
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
