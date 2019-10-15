"""Cache module"""

import os.path

_DEFAULT_CACHE_FILENAME = '~/sodigest'

def get_last_date() -> int:
    """
    Get the last cached date in Unix time.

    Args:
        None

    Returns:
        int: Last date from cache.
    """

    if not os.path.exists(os.path.expanduser(_DEFAULT_CACHE_FILENAME)):
        return None

    with open(os.path.expanduser(_DEFAULT_CACHE_FILENAME)) as cache_file:
        lines = cache_file.readlines()

    if not lines:
        return None

    return int(lines[0])

def set_last_date(last_date: int) -> None:
    """
    Cache the last date.

    Args:
        last_date (int): Last date to cache.

    Returns:
        None
    """

    with open(os.path.expanduser(_DEFAULT_CACHE_FILENAME), 'w+') as cache_file:
        cache_file.write(str(last_date))
