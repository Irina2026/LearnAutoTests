from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class SliderPage(BasePage):
    PATH = "/horizontal_slider"

    def __init__(self, page: Page):
        super().__init__(page)

        self.slider = WebElement(page=page,
                                 locator=self.page.locator("input[type='range']"),
                                 description="Slider button",
                                 )

        self.result_value = WebElement(page=page,
                                       locator=self.page.locator("#range"),
                                       description="Slider result",
                                       )

    def focus_slider_and_use_arrow_key(self, key: str, count: int):
        self.slider.focus()
        for _ in range(count):
            self.slider.press(key)
        return self.result_value.get_inner_text()

    def get_step(self) -> float:
        return float(self.slider.get_attribute("step"))

