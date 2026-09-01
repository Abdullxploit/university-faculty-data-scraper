import logging
import os
from config import LOG_FOLDER

os.makedirs(LOG_FOLDER, exist_ok=True)

def get_logger():
    logging.basicConfig(level=logging.INFO,
                            filename=f"{LOG_FOLDER}/app.log",
                            encoding="utf8",
                            format="%(asctime)s | %(levelname)s | %(filename)s | %(message)s")
    return logging.getLogger(__name__)


