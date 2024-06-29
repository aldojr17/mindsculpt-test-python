from .logging.logger import Logger

logger = Logger()


def get_logger():
    return logger.logger
