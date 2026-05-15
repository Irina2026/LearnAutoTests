import pytest

from core.config_reader import ConfigReader


@pytest.fixture(scope="session")
def config() -> ConfigReader:
    return ConfigReader()


@pytest.fixture(scope="session")
def base_url(config):
    return config.environment.get("base_url")
