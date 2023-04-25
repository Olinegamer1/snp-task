from datetime import datetime, timedelta
from tasks.task_05 import date_in_future
from constants import FORMAT_DATE


def test_date_in_future():
    assert date_in_future(5) == (datetime.now() + timedelta(days=5)).strftime(FORMAT_DATE)
    assert date_in_future(0) == datetime.now().strftime(FORMAT_DATE)
    assert date_in_future(-1) == (datetime.now() + timedelta(days=-1)).strftime(FORMAT_DATE)
    assert date_in_future(2.5) == datetime.now().strftime(FORMAT_DATE)
    assert date_in_future(-3.7) == datetime.now().strftime(FORMAT_DATE)


if __name__ == '__main__':
    test_date_in_future()
