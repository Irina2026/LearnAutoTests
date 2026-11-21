import logging

from playwright.sync_api import Page, Locator

from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)

"""
Класс действий с элементом
"""


class WebElement:
    def __init__(self, page: Page, locator: Locator, description: str) -> None:
        self.page = page
        self.locator = locator
        self.description = description

    def __str__(self) -> str:
        return f"WebElement[{self.description}]"

    def get_inner_text(self) -> str:
        logger.info(f"{self}: get inner text")
        result = self.locator.inner_text()
        logger.info(f"{self}: inner text = '{result}'")
        return result

    def click(self) -> None:
        logger.info(f"{self}: click")
        self.locator.click()

    def right_click(self) -> None:
        logger.info(f"{self}: right click")
        self.locator.click(button="right")

    def focus(self) -> None:
        logger.info(f"{self}: focus")
        self.locator.focus()

    def press(self, key: str) -> None:
        logger.info(f"{self}: press {key}")
        self.locator.press(key)

    def get_text_content(self) -> str:
        logger.info(f"{self}: get text content")
        result = self.locator.text_content()
        logger.info(f"{self}: text content = '{result}'")
        return result

    def get_attribute(self, attribute: str) -> str:
        logger.info(f"{self}: get attribute '{attribute}'")
        result = self.locator.get_attribute(attribute)
        logger.info(f"{self}: attribute '{attribute}' = '{result}'")
        return result

    def fill(self, value: str) -> None:
        logger.info(f"{self}: fill '{value}'")
        self.locator.fill(value)

    def input_value(self) -> str:
        logger.info(f"{self}: get input value")
        result = self.locator.input_value()
        logger.info(f"{self}: input value = '{result}'")
        return result

    def hover(self) -> None:
        logger.info(f"{self}: hover")
        self.locator.hover()

    def scroll_into_view(self) -> None:
        logger.info(f"{self}: scroll into view")
        self.locator.scroll_into_view_if_needed()

    def set_input_files(self, path: str) -> None:
        logger.info(f"{self}: set input files '{path}'")
        self.locator.set_input_files(path)