from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from core.tests.helpers.task_helper_test import CategoryFactory, TagFactory, TaskFactory
from mocks.api_routes_mock import ApiRouteMocks as routes


class TaskCategoryFilterAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_tasks_category(self):
        res = self.client.get(routes.url_api_get_tasks_by_category(self, 1))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_task_by_category_detail(self):
        task = TaskFactory(tags=[TagFactory()], category=CategoryFactory())
        res = self.client.get(routes.url_api_get_tasks_by_category(self, task.category.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data[0]['category'], task.category.id)

    def test_method_not_allowed_task_by_category_post(self):
        res = self.client.post(routes.url_api_get_tasks_by_category(self, 25))
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_task_by_category_0(self):
        res = self.client.get(routes.url_api_get_tasks_by_category(self, 25))
        self.assertEqual(len(res.data), 0)


class TaskTagsFilterAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_tasks_tags(self):
        res = self.client.get(routes.url_api_get_tasks_by_tags(self, 1))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_task_by_tags_detail(self):
        tag = TagFactory()
        task = TaskFactory(tags=[tag], category=CategoryFactory())
        res = self.client.get(routes.url_api_get_tasks_by_tags(self, tag.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data[0]['category'], task.category.id)
        self.assertEqual(res.data[0]['name'], task.name)
        self.assertTrue(len(res.data) > 0)
        self.assertEqual(res.data[0]['tags'][0], tag.id)

    def test_method_not_allowed_task_by_tags_post(self):
        res = self.client.post(routes.url_api_get_tasks_by_tags(self, 25))
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_task_by_tags_0(self):
        res = self.client.get(routes.url_api_get_tasks_by_tags(self, 20))
        self.assertEqual(len(res.data), 0)
