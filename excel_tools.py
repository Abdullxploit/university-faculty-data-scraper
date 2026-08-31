import logging
from pathlib import Path
from openpyxl import Workbook


logger = logging.getLogger(__name__)

def save_to_excel(records):
    if not records:
        logger.warning("No records to save to excel")
        return False

    output_path = Path("output") / "universities.xlsx"
    output_path.parent.mkdir(parents=True, exist_ok=True)


    try:
        workbook = Workbook()
        sheet = workbook.active

        fieldnames = [
            "University",
            "Faculty",
            "Department",
            "Name",
            "Position",
            "Image_url",
            "Image_file"
        ]
        sheet.append(fieldnames)

        for record in records:
            row = [(record.get(field, ""))for field in fieldnames]
            sheet.append(row)
            for column in sheet.columns:
                max_length = 0

                for cell in column:
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))

                column_letter = column[0].column_letter
                sheet.column_dimensions[column_letter].width = max_length + 2
        workbook.save(output_path)

        logger.info("Successfully saved %s records to Excel: %s",
                    len(records),
                    output_path)
        return True
    except OSError as error:
        logger.error("Failed to save excel file: %s",
                     error)
        return False




