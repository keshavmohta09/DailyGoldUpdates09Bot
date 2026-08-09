import json
import os

FILE_PATH = "data/latest.json"


def load_previous_data():

    if not os.path.exists(FILE_PATH):
        return {}

    with open(FILE_PATH, "r") as f:
        return json.load(f)


def save_current_data(data):

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)