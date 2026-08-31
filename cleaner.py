def clean_record(record):
    for key, value in record.items():
        if isinstance(value, str):
            record[key] = value.strip()


    return record

def is_valid_record(record):
    name = record.get("Name")
    university = record.get("University")

    if not name or not university:
        return False
    else:
        return True

