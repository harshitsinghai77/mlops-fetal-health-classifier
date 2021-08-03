import json

from utils.constant import DF_COLUMNS


def check_columns_exists(payload):
    """Check if dict contains the required key."""
    cols = payload.keys()
    return all(elem in cols for elem in DF_COLUMNS)


def load_file(file_path):
    with open(file_path) as json_file:
        payload = json.load(json_file)
    return payload