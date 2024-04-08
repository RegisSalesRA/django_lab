from django.test import SimpleTestCase
from calc import add, remove


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = add(5, 6)

        self.assertEqual(res, 11)

    def test_remove_numbers(self):
        res = remove(7, 6)

        self.assertEqual(res, 2)
