from typing import Tuple, Mapping, Any

from playwright.sync_api import Browser, BrowserContext, Page, ViewportSize


class PageFactory:
    DEFAULT_VIEWPORT = {"width": 1440, "height": 900}
    DEFAULT_IGNORE_HTTPS_ERRORS = True
    DEFAULT_TIMEOUT_MS = 10_000
    DEFAULT_NAVIGATION_TIMEOUT_MS = 15_000
    DEFAULT_ENABLE_TRACING = True
    DEFAULT_BLOCK_ANALYTICS = True

    def __init__(self, browser: Browser, config: Mapping[str, Any]):
        """
        Принимаем Mapping (например, dict или MappingProxyType),
        чтобы подчеркнуть, что конфиг не должен модифицироваться.
        """
        self.browser = browser
        self.config = config

    def create_page(self, http_credentials: dict | None = None) -> Tuple[BrowserContext, Page]:
        """
        Создает и настраивает контекст и страницу.
        Возвращает кортеж (context, page), чтобы вызывающий код мог корректно
        закрыть контекст после завершения теста (избежание утечек памяти).

        :param http_credentials: опциональные credentials для HTTP Basic Auth
            (например, {"username": "admin", "password": "admin"}).
            По умолчанию None — контекст создаётся без авторизации.
        """
        context = self._create_context(http_credentials=http_credentials)
        page = context.new_page()

        page.set_default_timeout(self.config.get("default_timeout_ms", self.DEFAULT_TIMEOUT_MS))
        page.set_default_navigation_timeout(
            self.config.get("navigation_timeout_ms", self.DEFAULT_NAVIGATION_TIMEOUT_MS)
        )

        return context, page

    def _create_context(self, http_credentials: dict | None = None) -> BrowserContext:

        viewport_config = self.config.get("viewport", self.DEFAULT_VIEWPORT)
        viewport: ViewportSize = {"width": viewport_config["width"], "height": viewport_config["height"]}

        context = self.browser.new_context(
            base_url=self.config.get("base_url"),
            viewport=viewport,
            ignore_https_errors=self.config.get("ignore_https_errors", self.DEFAULT_IGNORE_HTTPS_ERRORS),
            http_credentials=http_credentials,
        )

        if self.config.get("enable_tracing", self.DEFAULT_ENABLE_TRACING):
            context.tracing.start(screenshots=True, snapshots=True, sources=True)

        if self.config.get("block_analytics", self.DEFAULT_BLOCK_ANALYTICS):
            blocked_domains = self.config.get("blocked_domains", [])

            def handle_route(route):
                url = route.request.url
                if any(domain in url for domain in blocked_domains):
                    route.abort()
                else:
                    route.continue_()

            context.route("**/*", handle_route)

        return context
