from django.test import TestCase
from core.models import Task


class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Task.objects.create(name='django')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Task))
        self.assertEqual(str(d), 'django')