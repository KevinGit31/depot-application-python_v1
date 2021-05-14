import os
import json

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file_machine = os.path.join(THIS_FOLDER, 'file.json')


def read_bd():
    """
        Methode permettant d'aller lire les données qui se trouve dans notre fichier
    :return:
    """
    with open(file_machine, "r") as read_file:
        return json.load(read_file)


def write_bd(data):
    """
        Methode permettant de mettre à jour
    :param data: list data qu'on va mettre dans notre fichier
    :return:
    """
    with open(file_machine, "w", encoding="utf-8") as read_file:
        json.dump(data, read_file, ensure_ascii=False, indent=4)
    read_file.close()

