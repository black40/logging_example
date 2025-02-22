from os import path, remove
import logging


file_name = 'logs.log'


if path.isfile(file_name):
    remove(file_name)


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

log_handler = logging.FileHandler(file_name)
log_handler.setLevel(logging.DEBUG)

log_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

log_handler.setFormatter(log_formatter)
logger.addHandler(log_handler)

logger.info('Logging setup is complete...')
