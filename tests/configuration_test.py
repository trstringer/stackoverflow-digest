"""Configuration tests"""

import os
from unittest.mock import patch
from sodigest.configuration import Configuration

_CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'sodigest.yml')

def test_root_url():
    config = Configuration(config_path=_CONFIG_PATH)
    assert config.root_url(), 'URL should be defined'

def test_tags():
    config = Configuration(config_path=_CONFIG_PATH)
    assert config.tags(), 'Tags should not be None'

def test_sites():
    config = Configuration(config_path=_CONFIG_PATH)
    sites = config.sites()
    assert sites, 'Sites should not be None'
    assert isinstance(sites, list), 'Sites should be a list'
    assert len(sites) > 1, 'There should be multiple sites defined'
