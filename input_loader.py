import csv
import os
from config import INPUT_FOLDER

def load_universities():
    path = os.path.join(INPUT_FOLDER, "Universities.csv")
    universities = []

    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            universities.append(row)

    return universities

load_universities()
