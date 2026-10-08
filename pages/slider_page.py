from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class SliderPage(BasePage):
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

    def get_min(self) -> float:
        return float(self.slider.get_attribute("min"))

    def get_max(self) -> float:
        return float(self.slider.get_attribute("max"))

    def get_step(self) -> float:
        return float(self.slider.get_attribute("step"))

    def set_value(self, target_value: float) -> str:
        """Выставляет целевое значение слайдера, сам выбирая направление."""
        current_value = self.get_value()
        step = self.get_step()

        steps_count = round(abs(target_value - current_value) / step)
        key = "ArrowRight" if target_value >= current_value else "ArrowLeft"

        self.slider.focus()
        for _ in range(steps_count):
            self.slider.press(key)

        return self.result_value.get_inner_text()

    def get_value(self) -> float:
        return float(self.slider.input_value())
