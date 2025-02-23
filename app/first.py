import logging


logger = logging.getLogger(__name__)


class First:
    def __init__(self):
        logger.info('init class First')
        self.current_number = 0

    def increment_number(self):
        self.current_number += 1

    def decrement_number(self):
        self.current_number -= 1
