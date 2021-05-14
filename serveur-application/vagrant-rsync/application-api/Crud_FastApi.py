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


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:
        return False
    return True
