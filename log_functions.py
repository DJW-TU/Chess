from timeit import default_timer as timer
from functools import wraps
import logging
import logging.config
import json


with open("log_config.json") as f:
    config_dict = json.load(f)
    logging.config.dictConfig(config_dict)


def log_init(sec):
    with open("log_config.json") as f:
        config_dict = json.load(f)
        logging.config.dictConfig(config_dict)
    return logging.getLogger(sec)


logger = log_init(__name__)


def timeit(func: callable):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        logger.info(f"{func.__name__} took {round(end - start,5)} to execute")
        return result

    return wrap
