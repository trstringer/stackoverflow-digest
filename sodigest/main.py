"""Main entry point"""

import argparse
from datetime import datetime, timedelta
import time
from .cache import get_last_date, set_last_date
from .configuration import Configuration
from .data import questions_from_site

def main() -> None:
    """
    Main entry point.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config-file',
        help='configuration file (default /etc/sodigest.yml)'
    )
    parser.add_argument(
        '-l', '--last-day',
        action='store_true',
        help='get questions from the last 24 hours'
    )
    parser.add_argument(
        '-r', '--show-resolved',
        action='store_true',
        help='show resolved questions (ones that have an accepted answer)'
    )
    parser.add_argument(
        '-t', '--top',
        default=100,
        type=int,
        help='get top results per site (default to 100)'
    )
    args = parser.parse_args()

    config_file = args.config_file if args.config_file else None
    from_unix_date = None
    cached_date = get_last_date()
    last_day = int(time.mktime((datetime.now() - timedelta(days=1)).timetuple()))

    if args.last_day:
        from_unix_date = last_day
    elif cached_date:
        from_unix_date = cached_date
    # If the user didn't specify anything and there is no cached date then
    # just take questions from the past day anyways.
    else:
        from_unix_date = last_day

    config = Configuration(config_path=config_file)

    output = ''
    for site in config.sites():
        for question in questions_from_site(
                url=config.root_url(),
                site=site,
                tags=config.tags(),
                from_unix_date=from_unix_date,
                top=args.top,
                show_resolved=args.show_resolved):
            output += question.prettify()

    print(output)

    # Cache the last time this was run.
    set_last_date(last_date=int(time.time()))

if __name__ == '__main__':
    main()
