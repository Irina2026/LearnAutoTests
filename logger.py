import logging
import sys

LOGGER_NAME = "autotests"

def setup_logger(name: str = LOGGER_NAME, log_file: str = "tests.log", level=logging.DEBUG) -> logging.Logger:
    """
       Создаёт и настраивает логгер.
       :param name: имя логгера (обычно __name__ модуля)
       :param log_file: путь к файлу логов
       :param level: уровень логирования (DEBUG/INFO/WARNING/ERROR/CRITICAL)
       :return: экземпляр logging.Logger
       """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Формат сообщения: время - имя логгера - уровень - сообщение

    formatter = logging.Formatter(
        "%(asctime)s - [%(name)s] - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    """Консольный обработчик"""
    console_handler = logging.StreamHandler(sys.stdout)  # выводит логи в консоль
    console_handler.setLevel(logging.INFO)  # только логи INFO и выше
    console_handler.setFormatter(formatter)  # применить форматтер

    """Файловый обработчик"""
    file_handler = logging.FileHandler(log_file,
                                       encoding="utf-8")  # запись в файл в текущей директории с поддержкой кириллицы
    """
    FileHandler - простой, все логи в один файл, растет бесконечно
    RotatingFileHandler - ротация по размеру, maxBytes - размер, после превышения закрывается, backupCount - лимит на количество
    TimedRotatingFileHandler - ротация по хронологии
    """
    file_handler.setLevel(logging.DEBUG)  # все уровни
    file_handler.setFormatter(formatter)  # применить форматтер

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        # logger.propagate = False ???
    return logger
