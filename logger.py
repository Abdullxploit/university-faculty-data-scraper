import logging
from config import LOG_FOLDER


def get_logger():
    logging.basicConfig(level=logging.INFO,
                            filename=f"{LOG_FOLDER}/app.log",
                            encoding="utf8",
                            format="%(asctime)s | %(levelname)s | %(filename)s | %(message)s")
    return logging.getLogger(__name__)


