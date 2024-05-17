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

    def test_method_not_allowed_post(self):
        res = self.client.post(routes.url_api_get_task(24))
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_task(self):
        category = CategoryFactory()
        tag = TagFactory()
        payload = {
            'name': 'New Task',
            'description': 'Task description',
            'category': category.id,
            'tags': [tag.id]
        }
        res = self.client.post(routes.url_api_get_tasks(), payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], payload['name'])

    def test_create_task_missing_fields(self):
        payload = {
            'name': 'New Task'
        }
        res = self.client.post(routes.url_api_get_tasks(), payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_task(self):
        task = TaskFactory(tags=[TagFactory()], category=CategoryFactory())
        payload = {
            'name': 'Updated Task',
            'description': 'Updated description',
            'category': task.category.id,
            'tags': [tag.id for tag in task.tags.all()]
        }
        res = self.client.put(routes.url_api_get_task(task.id), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], payload['name'])

    def test_update_task_missing_fields(self):
        task = TaskFactory(tags=[TagFactory()], category=CategoryFactory())
        payload = {
            'name': ''
        }
        res = self.client.put(routes.url_api_get_task(task.id), payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_task_404(self):
        payload = {
            'name': 'Updated Task',
            'description': 'Updated description',
        }
        res = self.client.put(routes.url_api_get_task(20), payload)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_task(self):
        task = TaskFactory(tags=[TagFactory()], category=CategoryFactory())
        res = self.client.delete(routes.url_api_get_task(task.id))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_task_404(self):
        res = self.client.delete(routes.url_api_get_task(20))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)


class CategoryAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
