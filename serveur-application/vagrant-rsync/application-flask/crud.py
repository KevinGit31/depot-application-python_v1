import bdd_file
import Machine

listMachinesFomFile = []
listMachinesFomFile = bdd_file.read_bd()


def create_machine():
    pass


def get_machine(hostname):
    for machine in listMachinesFomFile:
        if machine["hostname"] == hostname:
            instance_machine = Machine.Machine(machine["id"], machine["hostname"], machine["ip"], machine["nombre_cpu"],
                                               machine["taille_ram"], machine["nombre_disque_dur"],
                                               machine["taille_disque_dur"], machine["os"], machine["version_os"])
        return {"id": instance_machine.id,
                "hostname": instance_machine.hostname,
                "ip": instance_machine.ip,
                "nombre cpu": instance_machine.nombre_cpu,
                "taille ram": instance_machine.taille_ram,
                "nombre disque dur": instance_machine.nombre_disque_dur,
                "taille disque dur": instance_machine.taille_disque_dur,
                "os": instance_machine.os,
                "version os": instance_machine.version_os}


def update_machine(hostname):
    pass


def delete_machine(hostname):
    for machine in listMachinesFomFile:
        if machine["hostname"] == hostname:
            listMachinesFomFile.remove(1)
    print(listMachinesFomFile)


def get_machines():
    lstObjMachine = []
    lstDataMachine = []
    for machine in listMachinesFomFile:
        instance_machine = Machine.Machine(machine["id"], machine["hostname"], machine["ip"], machine["nombre_cpu"],
                                           machine["taille_ram"], machine["nombre_disque_dur"],
                                           machine["taille_disque_dur"], machine["os"], machine["version_os"])
        lstObjMachine.append(instance_machine)
    for data in lstObjMachine:
        lstDataMachine.append(str(data.id) + " " + str(
            data.hostname) + " " + str(
            data.ip) + " " + str(
            data.nombre_cpu) + " " + str(
            data.taille_ram) + " " + str(
            data.nombre_disque_dur) + " " + str(
            data.taille_disque_dur) + " " + str(data.os) + " " + str(data.version_os))
    return lstDataMachine
    # return {"Liste listMachie": listMachinesFomFile}
