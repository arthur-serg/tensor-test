from loguru import logger
from datetime import datetime
import os


class Logger():

    def __init__(self):
        log_filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f.log')
        if (os.path.isdir("logs")):
            os.chdir("logs")
            logger.add(log_filename)

    pass
