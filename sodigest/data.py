"""Retrieve data from StackOverflow"""

from typing import Iterator, List
import requests

# pylint: disable=too-few-public-methods
class Question:
    """Store the question data."""

    def __init__(
            self,
            title: str,
            url: str,
            is_resolved: bool,
            tags: List[str]):
        """Initialize the question."""

        self._title = title
        self._tags = tags
        self._url = url
        self._is_resolved = is_resolved

    def prettify(self) -> str:
        """
        Format the question in a nice string.

        Args:
            None

        Returns:
            str: Prettified question string.
        """

        return '{}\n{}\n{}\n\n'.format(self._title, self._url, self._tags)

# pylint: disable=too-many-arguments
def questions_from_site(
        url: str,
        site: str,
        tags: List[str],
        from_unix_date: int,
        top: int,
        show_resolved: bool) -> Iterator[Question]:
    """
    Retrieve questions from a site.

    Args:
        url (str): URL of the site.
        site (str): Site name.
        from_unix_date (int): Unix epoch time.

    Returns:
        Iterator[Question]: Questions from the site.
    """

    url = url.rstrip('/')
    tags_formatted = ';'.join(tags)

    has_more = True
    page = 1
    question_count = 0
    while has_more and page < 10:
        # pylint: disable=line-too-long
        req_url = '{}/questions?fromdate={}&order=desc&sort=activity&tagged={}&site={}&page={}&pagesize=100'.format(
            url, from_unix_date, tags_formatted, site, page
        )
        response = requests.get(req_url)

        if response.status_code != 200:
            raise Exception('Error requesting {}: {}'.format(req_url, response.status_code))

        res_json = response.json()
        has_more = res_json['has_more']
        page += 1

        # Keep the max amount of questions below the top limit.
        if res_json['items'] and (question_count + len(res_json['items'])) > top:
            res_json['items'] = res_json['items'][:top - question_count]
            has_more = False

        yield from (
            Question(
                title=res_question['title'],
                url=res_question['link'],
                is_resolved=res_question.get('accepted_answer_id') is not None,
                tags=res_question['tags']
            )
            for res_question
            in res_json['items']
            if not res_question.get('accepted_answer_id')
            or show_resolved
        )
