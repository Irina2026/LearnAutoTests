import logging
from logger import LOGGER_NAME
from playwright.sync_api import Page, Locator
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