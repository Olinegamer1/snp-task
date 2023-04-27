import unittest
from datetime import datetime, timedelta
from tasks.task_05 import date_in_future
from constants import FORMAT_DATE


class TestDateInFuture(unittest.TestCase):

    def test_five_days_in_future(self):
        self.assertEqual(date_in_future(5), (datetime.now() + timedelta(days=5)).strftime(FORMAT_DATE))

    def test_today(self):
        self.assertEqual(date_in_future(0), datetime.now().strftime(FORMAT_DATE))

    def test_yesterday(self):
        self.assertEqual(date_in_future(-1), (datetime.now() + timedelta(days=-1)).strftime(FORMAT_DATE))

    def test_decimal_number_of_days(self):
        self.assertEqual(date_in_future(2.5), datetime.now().strftime(FORMAT_DATE))

    def test_negative_decimal_number_of_days(self):
        self.assertEqual(date_in_future(-3.7), datetime.now().strftime(FORMAT_DATE))
