from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from core.tests.helpers.task_helper_test import CategoryFactory, TagFactory, TaskFactory
from mocks.api_routes_mock import ApiRouteMocks as routes


class TaskAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_tasks(self):
        res = self.client.get(routes.url_api_get_tasks(self))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_task_detail(self):
        task = TaskFactory(tags=[TagFactory()], category=CategoryFactory())
        res = self.client.get(routes.url_api_get_task(self, task.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], task.name)

    def test_get_task_404(self):
        res = self.client.get(routes.url_api_get_task(self, 20))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_method_not_allowed_post(self):
        res = self.client.post(routes.url_api_get_task(self, 24))
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
        res = self.client.post(routes.url_api_get_tasks(self), payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], payload['name'])

    def test_create_task_missing_fields(self):
        payload = {
            'name': 'New Task'
        }
        res = self.client.post(routes.url_api_get_tasks(self), payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_task(self):
        task = TaskFactory(tags=[TagFactory()], category=CategoryFactory())
        payload = {
            'name': 'Updated Task',
            'description': 'Updated description',
            'category': task.category.id,
            'tags': [tag.id for tag in task.tags.all()]
        }
        res = self.client.put(routes.url_api_get_task(self, task.id), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], payload['name'])

    def test_update_task_missing_fields(self):
        task = TaskFactory(tags=[TagFactory()], category=CategoryFactory())
        payload = {
            'name': ''
        }
        res = self.client.put(routes.url_api_get_task(self, task.id), payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_task_404(self):
        payload = {
            'name': 'Updated Task',
            'description': 'Updated description',
        }
        res = self.client.put(routes.url_api_get_task(self, 20), payload)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_task(self):
        task = TaskFactory(tags=[TagFactory()], category=CategoryFactory())
        res = self.client.delete(routes.url_api_get_task(self, task.id))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_task_404(self):
        res = self.client.delete(routes.url_api_get_task(self,  20))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)


class CategoryAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_categorys(self):
        res = self.client.get(routes.url_api_get_categories(self))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_category_detail(self):
        category = CategoryFactory()
        res = self.client.get(routes.url_api_get_category(self,  category.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], category.name)

    def test_get_task_404(self):
        res = self.client.get(routes.url_api_get_category(self,  20))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_method_not_allowed_post(self):
        res = self.client.post(routes.url_api_get_category(self, 24))
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_category(self):
        payload = {
            'name': 'New Task',
        }
        res = self.client.post(routes.url_api_get_categories(self), payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], payload['name'])

    def test_create_category_missing_fields(self):
        payload = {
            'name': ''
        }
        res = self.client.post(routes.url_api_get_categories(self), payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_category(self):
        category = CategoryFactory()
        payload = {
            'name': 'Updated category',
        }
        res = self.client.put(routes.url_api_get_category(self, category.id), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], payload['name'])

    def test_update_category_missing_fields(self):
        category = CategoryFactory()
        payload = {
            'name': ''
        }
        res = self.client.put(routes.url_api_get_category(self, category.id), payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_category_404(self):
        payload = {
            'name': 'Updated category',
            'description': 'Updated description',
        }
        res = self.client.put(routes.url_api_get_category(self, 20), payload)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_category(self):
        category = CategoryFactory()
        res = self.client.delete(routes.url_api_get_category(self, category.id))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_category_404(self):
        res = self.client.delete(routes.url_api_get_category(self, 20))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)


class TagAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_tags(self):
        res = self.client.get(routes.url_api_get_tags(self))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_tag_detail(self):
        tag = TagFactory()
        res = self.client.get(routes.url_api_get_tag(self, tag.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], tag.name)

    def test_get_task_404(self):
        res = self.client.get(routes.url_api_get_tag(self, 20))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_method_not_allowed_post(self):
        res = self.client.post(routes.url_api_get_tag(self, 24))
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_tag(self):
        payload = {
            'name': 'New Task',
        }
        res = self.client.post(routes.url_api_get_tags(self), payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], payload['name'])

    def test_create_tag_missing_fields(self):
        payload = {
            'name': ''
        }
        res = self.client.post(routes.url_api_get_tags(self), payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_tag(self):
        tag = TagFactory()
        payload = {
            'name': 'Updated tag',
        }
        res = self.client.put(routes.url_api_get_tag(self, tag.id), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], payload['name'])

    def test_update_tag_missing_fields(self):
        tag = TagFactory()
        payload = {
            'name': ''
        }
        res = self.client.put(routes.url_api_get_tag(self, tag.id), payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_tag_404(self):
        payload = {
            'name': 'Updated tag',
            'description': 'Updated description',
        }
        res = self.client.put(routes.url_api_get_tag(self, 20), payload)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_tag(self):
        tag = TagFactory()
        res = self.client.delete(routes.url_api_get_tag(self, tag.id))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_tag_404(self):
        res = self.client.delete(routes.url_api_get_tag(self, 20))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
