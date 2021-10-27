import logging


log_level = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
}

logging.basicConfig(
    level="INFO",
    format="[%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)


def info(message):
    logging.info(message)


def debug(message):
    logging.debug(message)
