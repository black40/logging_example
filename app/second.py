import logging


class Second:
    def __init__(self):
        self.enabled = False

    def enable_system(self):
        self.enabled = True

    def disable_system(self):
        self.enabled = False
