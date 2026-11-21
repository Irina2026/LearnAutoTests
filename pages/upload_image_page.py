from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class UploadImagePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.file_input = WebElement(
            page=page,
            locator=page.locator("#file-upload"),
            description="File input",
        )
        self.submit_button = WebElement(
            page=page,
            locator=page.locator("#file-submit"),
            description="Upload button",
        )
        self.heading = WebElement(
            page=page,
            locator=page.locator(".example h3"),
            description="Heading",
        )
        self.file_name = WebElement(
            page=page,
            locator=page.locator("#uploaded-files"),
            description="File name",
        )

    def upload_file(self, file_path: str) -> None:
        self.file_input.set_input_files(file_path)
        self.submit_button.click()

    def get_heading(self) -> str:
        return self.heading.get_inner_text()

    def get_file_name(self) -> str:
        return self.file_name.get_inner_text()