from datetime import datetime

from utils.constants import DateTimeConstants


def get_datetime(value, measure):
    """
    :param measure: time measurement is input value in seconds or milliseconds?
    :type measure: str
    :param value: timestamp to be converted
    :type value: int
    """
    if measure == DateTimeConstants.MS:
        value = value/1000
    if measure == DateTimeConstants.S:
        # :)
        value = value

    # fromtimestamp expects the input in seconds
    return datetime.fromtimestamp(int(value))
