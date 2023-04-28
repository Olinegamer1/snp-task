import unittest
from task_11 import Dessert


class TestDessert(unittest.TestCase):

    def setUp(self):
        self.dessert = Dessert(name='Brownie', calories=500)

    def test_name(self):
        self.assertEqual(self.dessert.name, 'Brownie')

    def test_calories(self):
        self.assertEqual(self.dessert.calories, 500)

    def test_is_healthy(self):
        self.assertFalse(self.dessert.is_healthy())

    def test_is_delicious(self):
        self.assertTrue(self.dessert.is_delicious())

    def test_default_values(self):
        dessert = Dessert()
        self.assertEqual(dessert.name, 'unknown')
        self.assertEqual(dessert.calories, 0)

    def test_set_name(self):
        self.dessert.name = 'Chocolate Cake'
        self.assertEqual(self.dessert.name, 'Chocolate Cake')

    def test_set_calories(self):
        self.dessert.calories = 250
        self.assertEqual(self.dessert.calories, 250)
