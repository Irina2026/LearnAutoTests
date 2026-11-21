from playwright.sync_api import Page

from pages.windows_page import WindowsPage


def test_windows_page(managed_page: Page):

    managed_page.goto("/windows")
    page = WindowsPage(managed_page)


    tab1 = page.click_here_and_get_new_tab()
    assert page.get_heading(tab1) == "New Window", "Неверный текст в первой новой вкладке"
    """
    expect_page() переключает фокус на открытую вкладку, bring_to_front вызванный у первой вкладки из фикстуры
    возращает на исходную
    """
    managed_page.bring_to_front()


    tab2 = page.click_here_and_get_new_tab()
    assert page.get_heading(tab2) == "New Window", "Неверный текст во второй новой вкладке"


    managed_page.bring_to_front()


    tab1.close() #после закрытия вернуться нельзя, иначе Target closed, если закрыть активную, фокус перейдет на другую
    tab2.close()


    assert len(managed_page.context.pages) == 1, ( #context.pages - СПИСОК всех открытых в этом контексте
        f"Ожидали 1 вкладку, а открыто: {len(managed_page.context.pages)}"
    )