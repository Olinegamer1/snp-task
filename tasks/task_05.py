from datetime import datetime, timedelta
from constants import FORMAT_DATE


def date_in_future(days: int) -> str:
    """
    Return current date plus N count of days if days are the int.
    Otherwise, return current date.
    """

    date = datetime.now() + timedelta(days=days) if isinstance(days, int) else datetime.now()
    return date.strftime(FORMAT_DATE)
