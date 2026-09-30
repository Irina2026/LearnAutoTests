import logging
from logger import LOGGER_NAME
from playwright.sync_api import Page, Dialog
logger = logging.getLogger(LOGGER_NAME)
from collections.abc import Callable

"""
Класс действий со страницей
"""
class PageActions:
    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, url: str) -> None:
        logger.info(f"PageActions: goto '{url}'")
        self.page.goto(url)

    """
    Запускают какое-то действие (например, клик по кнопке, который вызывает диалог).
    Заранее настраивают обработчик этого диалога.
    После выполнения действия возвращают текст сообщения из диалога.
    """
    """
    Объявили пустую переменную
    Объявили функцию, но пока ее не вызвали
    Зарегистрировали эту функцию в реестр обработчиков Playwright
    Выполнили действие action()
    Код отправляет команду "click" в браузер
    Playwright ПРИОСТАНАВЛИВАЕТ поток (greenlet switch)
    Управление переходит в event loop Playwright
    Event loop ждёт ответы и события от браузера
    Браузер открывает диалог - происходит событие
    Приостанавливает JS на странице
    Отправляет событие в Playwright: Page.javascriptDialogOpening
    Playwright превращает это событие в диалог и проверяет реестр, handle_dialog найден
    Отрабатывает внутренняя функция
    Когда она вызывает dialog.accept(), это ещё одна команда браузеру, которая проходит через тот же event loop
    После этого обработчик завершается. Управление возвращается в event loop Playwright
    Браузер закрывает диалог, action() завершается, возвращает управление 
    --- Специально диалог не ждет, просто выполняет action, если внутри прошло событие - обрабатывается
    --- Может быть ограничено дефолтным таймаутом action, либо установленным в конфиге
    """
    def _handle_dialog(
            self,
            action: Callable[[], None], # действие(функция или вызываемый объект, не принимает аргументов,
                                        # ничего не возвращает)
            mode: str, # режим "accept" - ок, "dismiss" - отмена
            prompt_text: str | None = None, # необязательный ввод
    ) -> str:
        logger.info("PageActions: expect dialog")
        message = ""  # сюда сохраняется текст диалога

        def handle_dialog(dialog: Dialog) -> None:
            nonlocal message  # не создавать локальную, изменить внешнюю
            message = dialog.message
            logger.info(f"PageActions: dialog '{dialog.type}' with message '{message}'")
            if mode == "dismiss":
                dialog.dismiss()
                return

            if prompt_text is None:
                dialog.accept()
                return

            dialog.accept(prompt_text)

        self.page.once("dialog", handle_dialog) # подписаться один раз и закрыть, on - навсегда до закрытия
                                                        # страницы, предотвращает случайную обработку следующих диалогов
        """
        Триггер: выполнение функции, вызывающей диалог
        """
        action()

        if not message:
            raise RuntimeError("Expected dialog was not shown")

        return message

    def run_and_accept_alert(self, action: Callable[[], None]) -> str:
        logger.info("PageActions: accept dialog")
        return self._handle_dialog(action, mode="accept")

    def run_and_dismiss_alert(self, action: Callable[[], None]) -> str:
        logger.info("PageActions: dismiss dialog")
        return self._handle_dialog(action, mode="dismiss")

    def run_and_accept_prompt(
            self,
            action: Callable[[], None],
            prompt_text: str,
    ) -> str:
        logger.info("PageActions: accept prompt")
        return self._handle_dialog(action, mode="accept", prompt_text=prompt_text)

