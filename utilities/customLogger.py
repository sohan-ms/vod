import logging


class LogGen():
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
        file_handler = logging.FileHandler(".//Logs//automation.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
