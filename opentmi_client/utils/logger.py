"""
Logger module for OpenTMI client
"""
import logging


def get_logger(name="OpenTMI", level=logging.DEBUG):
    """
    Get opentmi logger
    :return: Logger
    """
    # use default logger
    logger = logging.getLogger(name)
    if logger.handlers == []:
        return logger

    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    stream_handler.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(stream_handler)
    return logger
