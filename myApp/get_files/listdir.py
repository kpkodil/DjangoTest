import os
from datetime import datetime
from .config import dir

def listdir() -> list:
    directory: str = dir
    file: str
    file_extension: str
    ts: float
    file_list: list = []
    file_object: dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_extension = file.split('.')[-1]
            file = os.path.splitext(file)[0]
            ts = os.path.getctime(directory)
            created_at = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
            file_object['name'] = file
            file_object['type'] = file_extension
            file_object['time'] = created_at
            file_list.append(file_object)
            file_object = {}
    return file_list
