"""
Корневой conftest для всех, если нужно что-то специфическое для определенной группы тестов, нужно разделить,
добавить локальный в папку с тестами
"""

import json
from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType

import pytest
from playwright.sync_api import Browser, Page

from logger import setup_logger
from page_factory import PageFactory


# Читаем конфиг ОДИН раз на весь сеанс (session)
@pytest.fixture(scope="session")
def app_config() -> Mapping:
    config_path = Path("config/config.json")
    if not config_path.is_file():
        raise FileNotFoundError(f"Файл конфигурации не найден: {config_path.resolve()}")

    with open(config_path, encoding="utf-8") as config_file:
        raw_config = json.load(config_file)

    if "base_url" not in raw_config:
        raise ValueError("В конфигурации отсутствует обязательный параметр 'base_url'")

    # MappingProxyType делает словарь read-only.
    # Если необходимо изменить конфиг - сделать простую копию, менять в ней
    return MappingProxyType(raw_config)


def _create_managed_page(
    browser: Browser,
    app_config: Mapping,
    http_credentials: dict | None = None,
) -> Page:
    """Создаёт контекст и страницу через единую фабрику и гарантирует очистку."""
    factory = PageFactory(browser=browser, config=app_config)

    context, page = factory.create_page(http_credentials=http_credentials)

    yield page

    # Очистка
    if app_config.get("enable_tracing", True):
        # Динамическое имя файла? request.node.name?
        context.tracing.stop(path=f"test-results/trace-{id(page)}.zip")

    context.close()


# Фикстура страницы: scope="function" - новая страница и контекст на каждый тест
@pytest.fixture(scope="function")
def managed_page(browser: Browser, app_config: Mapping) -> Page:
    # Создание экземпляра фабрики мгновенно, так как конфиг уже в памяти
    yield from _create_managed_page(browser, app_config)


# Фикстура страницы с HTTP Basic Auth: только те тесты, которым нужна авторизация,
# явно запрашивают эту фикстуру. Остальные тесты получают обычный контекст.
@pytest.fixture(scope="function")
def managed_page_with_auth(browser: Browser, app_config: Mapping) -> Page:
    yield from _create_managed_page(
        browser,
        app_config,
        http_credentials={"username": "admin", "password": "admin"},
    )


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()
