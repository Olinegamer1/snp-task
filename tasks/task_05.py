from datetime import datetime, timedelta
from constants import FORMAT_DATE


def date_in_future(days_amount: int) -> str:
    """
    Returns current date plus N count of days if days_amount are the int.
    Otherwise, returns current date.
    """

    date = datetime.now() + timedelta(days=days_amount)\
        if isinstance(days_amount, int) else datetime.now()
    return date.strftime(FORMAT_DATE)
