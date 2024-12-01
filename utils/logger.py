
import logging

def setup_logger(name, level=logging.INFO, log_file=None):
    """
    Sets up a logger with the given name, level, and optional file output.

    :param name: Logger name.
    :param level: Logging level (e.g., logging.INFO, logging.DEBUG).
    :param log_file: Optional file to save logs.
    :return: Configured logger.
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
