import csv
import logging
from pathlib import Path



logger = logging.getLogger(__name__)

def save_records(records):
    if not records:
        logger.warning("No Records to Save")
        return False
    try:
        output_path = Path("output")/"universities.csv"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fieldnames=["University",
                    "Faculty",
                    "Department",
                    "Name",
                    "Position",
                    "Image_url",
                    "Image_file"
                     ]

        with output_path.open("w", newline="",
                              encoding="utf-8") as file:
            writer = csv.DictWriter(file,
                                    fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)

            logger.info("successfully saved %s records to %s",
                        len(records),
                        output_path)
            return True


    except OSError as error:
        logger.error("Failed to save records to %s: %s",
                     output_path,
                     error)
        return False

def save_invalid_records(records):
    if not records:
        logger.warning("No invalid_record to save")
        return False

    try:
        output_path = Path("output")/ "invalid_records.csv"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        fieldnames = ["University",
                      "Faculty",
                      "Department",
                      "Name",
                      "Position",
                      "Image_url",
                      "Image_file"
                      ]

        with output_path.open("w", newline="",
                              encoding="utf8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(records)

        logger.info("Successfully saved %s invalid records to: %s",
                    len(records),
                    output_path)
        return True


    except OSError as error:
        logger.error("Failed to save invalid records: %s",
                     error)
        return False







