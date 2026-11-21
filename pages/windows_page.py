from playwright.sync_api import Page
from pages.base_page import BasePage
from ui.web_element import WebElement

class WindowsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.link = WebElement(page=page,
                               locator=self.page.get_by_role("link", name="Click Here"),
                               description="Link button")

    """
    Любой объект, у которого есть два метода — __enter__ и __exit__ 
    — называется менеджером контекста и его можно использовать с with
    with - синтаксический сахар над try/finally
    expect_* всегда оборачивает действие, которое должно вызвать событие
    """

    """
    (1)	Включает «прослушку»: «если в контексте появится новая вкладка — запомни её».
     Пока ничего не произошло, new_page_info.value ещё не готов.
    (2)	Клик по ссылке target="_blank". Браузер реально открывает новую вкладку. 
    Playwright ловит это событие. Ожидание завершается.
    (3)	Теперь new_page_info.value содержит готовый Page новой вкладки. С ним можно работать.
    """
    def click_here_and_get_new_tab(self) -> Page:
        """Клик по 'Click Here' → дождаться новой вкладки → вернуть её Page."""
        with self.page.context.expect_page() as new_page_info: # дождаться открытия expect page
            self.link.click() # нажать ссылку
        new_tab = new_page_info.value # это то, что вернул __enter__(), не сама вкладка, а объект-обертка до value
        new_tab.wait_for_load_state()  # дождаться загрузки страницы в новой вкладке
        return new_tab

    def get_heading(self, tab: Page) -> str:
        """Найти первый элемент с ролью 'заголовок' и вернуть видимый текст как строку"""

        return tab.get_by_role("heading").inner_text()