import json
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file_machine = os.path.join(THIS_FOLDER, 'file.json')


def read_bd():
    with open(file_machine, "r") as read_file:
        return json.load(read_file)


def write_bd(machine_json):
    with open(file_machine, "w", encoding="utf-8") as write_file:
        return json.dump(machine_json, write_file, ensure_ascii=False, indent=4)

