from pathlib import Path
import requests
import logging
from config import HEADERS


logger = logging.getLogger(__name__)



def download_image(image_url, image_name):
    try:
        output_directory = Path("output")/"images"
        output_directory.mkdir(parents=True, exist_ok=True)

        output_path = output_directory/image_name
        response = requests.get(image_url, timeout=30, headers=HEADERS)
        response.raise_for_status()

        output_path.write_bytes(response.content)
        logger.info("Successfully downloaded image for: %s",
                    image_name)
        return output_path
    except requests.RequestException as error:
        logger.error("Failed to download %s: %s",
                     image_url,
                     error)
        return None
    except OSError as error:
        logger.error("Failed to save image %s: %s",
                     image_url,
                     error)
        return None


def clean_filename(name):
    name = name.replace(" ", "_")
    name = name.replace("/", "_")
    name = name.replace("\\", "_")
    return name
