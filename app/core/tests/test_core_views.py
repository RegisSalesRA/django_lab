from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from mocks.api_routes_mock import ApiRouteMocks as routes


class TaskAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_task_values(self):
        res = self.client.get(routes.url_api_get_tasks())
        self.assertEqual(res.status_code, status.HTTP_200_OK)
