"""Main entry point"""

import argparse
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
    args = parser.parse_args()

    config_file = None

    if args.config_file:
        config_file = args.config_file
        print(f'Config path specified: {config_file}')

    config = Configuration(config_path=config_file)

    for site in config.sites():
        questions_from_site(
            url=config.root_url(),
            site=site,
            tags=config.tags(),
            from_unix_date=
        )

if __name__ == '__main__':
    main()
