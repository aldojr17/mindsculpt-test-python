import logging


class Logger:

    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
