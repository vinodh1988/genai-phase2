"""
Represents a duration expressing a difference between two dates or times.

timedelta objects represent a duration, the difference between two dates or times.
It is used to add or subtract time intervals from date and datetime objects.

Args:
    days (int, optional): Number of days. Default is 0.
    seconds (int, optional): Number of seconds. Default is 0.
    microseconds (int, optional): Number of microseconds. Default is 0.
    milliseconds (int, optional): Number of milliseconds. Default is 0.
    minutes (int, optional): Number of minutes. Default is 0.
    hours (int, optional): Number of hours. Default is 0.
    weeks (int, optional): Number of weeks. Default is 0.

Returns:
    timedelta: A timedelta object representing the total duration.

Example:
    >>> from datetime import timedelta
    >>> delta = timedelta(days=1, hours=2, minutes=30)
    >>> print(delta)
    1 day, 2:30:00

Note:
    Only keyword arguments are accepted. All arguments are converted to floating
    point numbers and rounded to the nearest microsecond. Any overflow is handled
    by carrying over to the next larger unit. Negative values are allowed.
"""