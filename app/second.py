import logging


logger = logging.getLogger(__name__)


class Second:
    def __init__(self):
        logger.info('init class Second')
        self.enabled = False

    def enable_system(self):
        self.enabled = True

    def disable_system(self):
        self.enabled = False
