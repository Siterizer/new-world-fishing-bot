from datetime import datetime
import logging
logging.basicConfig(filename="saved_data/logs/logs.log", level=logging.INFO)

def log(text):
    actual_time = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f: ')
    logging.info(actual_time + text)