"""Configuration module"""

from typing import List
import yaml

class Configuration:
    """Configuration class to handle all configuration."""

    def __init__(self, config_path: str = '/etc/sodigest.yml'):
        self._values = None
        self._load_config(config_path=config_path)

    def _load_config(self, config_path: str) -> None:
        """
        Load the configuration into memory.

        Args:
            config_path (str): Configuration file path.

        Returns:
            None
        """

        with open(config_path) as config_file:
            self._values = yaml.safe_load(config_file)

    def root_url(self) -> str:
        """
        Get the root StackOverflow URL.

        Args:
            None

        Returns:
            str: Root URL.
        """

        return self._values['url']

    def sites(self) -> List[str]:
        """
        Retrieve all sites to search.

        Args:
            None

        Returns:
            List[str]: All sites to search.
        """

        return self._values['sites']

    def tags(self) -> List[str]:
        """
        Retrieve all tags to search.

        Args:
            None

        Returns:
            List[str]: All tags to search.
        """

        return self._values['tags']
