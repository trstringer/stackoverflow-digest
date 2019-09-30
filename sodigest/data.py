"""Retrieve data from StackOverflow"""

import requests
from typing import Iterator, Dict, Any, List

def questions_from_site(
        url: str,
        site: str,
        tags: List[str],
        from_unix_date: int) -> Iterator[Dict[str, Any]]:
    """
    Retrieve questions from a site.

    Args:
        url (str): URL of the site.
        site (str): Site name.
        from_unix_date (int): Unix epoch time.

    Returns:
        Iterator[Dict[str, Any]]: Questions from the site.
    """

    url = url.rstrip('/')
    tags_formatted = ';'.join(tags)

    response = requests.get(f'{url}/questions?fromdate={from_unix_date}&order=desc&sort=activity&tagged={tags_formatted}&site={site}')

    import pdb; pdb.set_trace()
