import unittest
from tasks.task_12 import JellyBean


class TestJellyBean(unittest.TestCase):

    def test_getters(self):
        jellybean = JellyBean('JellyBean', 50, 'Lemon')
        self.assertEqual(jellybean.name, 'JellyBean')
        self.assertEqual(jellybean.calories, 50)
        self.assertEqual(jellybean.flavor, 'Lemon')

    def test_setters(self):
        jellybean = JellyBean('JellyBean', 50, 'Lemon')
        jellybean.name = 'Sour Patch Kids'
        jellybean.calories = 80
        jellybean.flavor = 'Watermelon'
        self.assertEqual(jellybean.name, 'Sour Patch Kids')
        self.assertEqual(jellybean.calories, 80)
        self.assertEqual(jellybean.flavor, 'Watermelon')

    def test_is_healthy(self):
        healthy_jellybean = JellyBean("Jelly Bean", 20, "Strawberry")
        unhealthy_jellybean = JellyBean("Jelly Bean", 270, "Black Licorice")
        self.assertTrue(healthy_jellybean.is_healthy())
        self.assertFalse(unhealthy_jellybean.is_healthy())

    def test_is_delicious(self):
        delicious_jellybean = JellyBean("Jelly Bean", 30, "Blueberry")
        self.assertTrue(delicious_jellybean.is_delicious())

        bad_flavored_jellybean = JellyBean("Jelly Bean", 30, "Black Licorice")
        self.assertFalse(bad_flavored_jellybean.is_delicious())
