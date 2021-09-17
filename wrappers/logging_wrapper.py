import logging
from utils.config import dict

log_level = {'DEBUG': logging.DEBUG,
             'INFO': logging.INFO,
            }

logging.basicConfig(
    level=log_level.get(dict['log_lvl']),
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

def info(message):
    logging.info(message)

def debug(message):
    logging.debug(message)