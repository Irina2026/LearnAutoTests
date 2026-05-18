from playwright.sync_api import Page

from core.config_reader import ConfigReader


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.config = ConfigReader()
       