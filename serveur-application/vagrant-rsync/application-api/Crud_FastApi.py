from fastapi.encoders import jsonable_encoder
import socket

import Machine
import bdd_file

listMachinesFomFile = []
listMachinesFomFile = bdd_file.read_bd()


def create_machine(machine: Machine):
    machine_dict = machine.dict()
    listMachinesFomFile.append(machine_dict)
    return bdd_file.write_bd(listMachinesFomFile)


def get_machines():
    return listMachinesFomFile


def get_machine(hostname):
    return listMachinesFomFile[return_index_machine(hostname)]


def update_machine(hostname, machine: Machine):
    update_item_encoded = jsonable_encoder(machine)
    listMachinesFomFile[return_index_machine(hostname)] = update_item_encoded
    bdd_file.write_bd(listMachinesFomFile)


def delete_machine(hostname):
    listMachinesFomFile.pop(return_index_machine(hostname))
    bdd_file.write_bd(listMachinesFomFile)


def return_index_machine(hostname):
    for machine in range(len(listMachinesFomFile)):
        if listMachinesFomFile[machine]["hostname"] == hostname:
            return machine


def is_exists_machine(hostname):
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
