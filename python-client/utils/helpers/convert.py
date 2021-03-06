from datetime import datetime

from utils.constants import DateTimeConstants


def get_datetime(value, measure):
    """
    :param measure: time measurement is input value in seconds or milliseconds?
    :type measure: str
    """
    value = get_time_value(measure, value)

    # fromtimestamp expects the input in seconds
    return datetime.fromtimestamp(int(value))


def get_time_value(measure, value):
    if measure == DateTimeConstants.MS:
        value = value / 1000
    if measure == DateTimeConstants.S:
        # :)
        value = value
    return value


def get_time(value, measure):
    value = get_time_value(measure, value)
    return datetime.fromtimestamp(int(value)).strftime("%H:%M:%S")



