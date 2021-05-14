from fastapi.encoders import jsonable_encoder
import socket

import Machine
import bdd_file

listMachinesFomFile = []
listMachinesFomFile = bdd_file.read_bd()


def create_machine(machine: Machine):
    """
        Methode qui va permettre de créer une nouvelle machine en entrant toutes les informations qui caracterisent une machine
    :return:
    """
    machine_dict = machine.dict()
    listMachinesFomFile.append(machine_dict)
    return bdd_file.write_bd(listMachinesFomFile)


def get_machines():
    """
        Methode qui va permettre de récupérer toutes les machines du parc informatique
    :return: listMachinesFomFile
    """
    return listMachinesFomFile


def get_machine(hostname):
    """
        Methode permettant de récupérer une machine à l'aide de son hostname
    :param hostname: nom de la machine
    :return: machine
    """
    return listMachinesFomFile[return_index_machine(hostname)]


def update_machine(hostname, machine: Machine):
    """
        Permet la mise à jour d'une machine existante à l'aide de son hostname
    :param hostname: nom de la machine sur laquelle on va faire les modifications
    :param machine: nouvelle machine
    :return:
    """
    update_item_encoded = jsonable_encoder(machine)
    listMachinesFomFile[return_index_machine(hostname)] = update_item_encoded
    return bdd_file.write_bd(listMachinesFomFile)


def delete_machine(hostname):
    """
        Methode permettant la suppression d'une machine à l'aide de son hostname
    :param hostname: nom de la machine
    :return:
    """
    listMachinesFomFile.pop(return_index_machine(hostname))
    bdd_file.write_bd(listMachinesFomFile)


def return_index_machine(hostname):
    """
            Verifier si l'hostname existe
        :param hostname: on récupère l'hostname saisi par l'utilisateur
        :return: index machine
        """
    for machine in range(len(listMachinesFomFile)):
        if listMachinesFomFile[machine]["hostname"] == hostname:
            return machine


def is_exists_machine(hostname):
    """
            Verifier si l'hostname existe
        :param hostname: on récupère l'hostname saisi par l'utilisateur
        :return: true si l'hostname existe et false sinon
        """
    for machine in range(len(listMachinesFomFile)):
        if listMachinesFomFile[machine]["hostname"] == hostname:
            return True
    return False


def is_valid_ipv4_address(ip):
    """
        Verifier si l'adresse ip est conforme
    :param ip: on récupère l'adresse ip saisi par l'utilisateur
    :return:
    """
    valid_or_not_valid = False
    tmp_ip = ip.split(".")
    i = 0
    if ip.count('.') == 3:
        valid_or_not_valid = True
    while valid_or_not_valid and i < len(tmp_ip):
        valid_or_not_valid = tmp_ip[i].isnumeric()
        i += 1
    if not valid_or_not_valid:
        print("Adresse ip invalid")
    return valid_or_not_valid
