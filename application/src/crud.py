import bdd_file
import Machine

listMachinesFomFile = []
listMachinesFomFile = bdd_file.read_bd()


def create_machine():
    """
        Permet de créer une nouvelle machine en entrant toutes les informations qui caracterisent une machine
    :return:
    """
    hostname, ip, cpu, ram, numberDD, spaceDD, os, version_os = verif_insert_user()
    new_machine = Machine.Machine(hostname, ip, cpu, ram, numberDD, spaceDD, os, version_os)
    data = {
        "hostname": new_machine.hostname,
        "ip": new_machine.ip,
        "nombre_cpu": new_machine.nombre_cpu,
        "taille_ram": new_machine.taille_ram,
        "nombre_disque_dur": new_machine.nombre_disque_dur,
        "taille_disque_dur": new_machine.taille_disque_dur,
        "os": new_machine.os,
        "version_os": new_machine.version_os
    }
    listMachinesFomFile.append(data)
    bdd_file.write_bd(listMachinesFomFile)


def get_machine(hostname):
    """
        Permet de recuperer les informations pour une machine donnée en parametre
    :param hostname: nom de la machine
    :return: json avec les informations lié au hostname de la machine
    """
    for machine in listMachinesFomFile:
        if machine["hostname"] == hostname:
            instance_machine = Machine.Machine(machine["hostname"], machine["ip"], machine["nombre_cpu"],
                                               machine["taille_ram"], machine["nombre_disque_dur"],
                                               machine["taille_disque_dur"], machine["os"], machine["version_os"])
            return {"hostname": instance_machine.hostname,
                    "ip": instance_machine.ip,
                    "nombre cpu": instance_machine.nombre_cpu,
                    "taille ram": instance_machine.taille_ram,
                    "nombre disque dur": instance_machine.nombre_disque_dur,
                    "taille disque dur": instance_machine.taille_disque_dur,
                    "os": instance_machine.os,
                    "version os": instance_machine.version_os}
    return "Impossible de trouver le hostname de la machine.\n"


def update_machine(hostname):
    """
        Permet la mise à jour d'une machine existante à l'aide de son hostname
    :param hostname: nom de la machine sur laquelle on va faire les modifications
    :return:
    """
    print("Bienvenue sur la console de mise à jour pour la machine " + hostname)
    for machine in range(len(listMachinesFomFile)):
        namehost = listMachinesFomFile[machine]["hostname"]
        if namehost == hostname:
            hostname, ip, cpu, ram, numberDD, spaceDD, os, version_os = verif_insert_user()
            new_machine = Machine.Machine(hostname, ip, cpu, ram, numberDD, spaceDD, os, version_os)
            listMachinesFomFile[machine]["hostname"] = new_machine.hostname
            listMachinesFomFile[machine]["ip"] = new_machine.ip
            listMachinesFomFile[machine]["nombre_cpu"] = new_machine.nombre_cpu
            listMachinesFomFile[machine]["taille_ram"] = new_machine.taille_ram
            listMachinesFomFile[machine]["nombre_disque_dur"] = new_machine.nombre_disque_dur
            listMachinesFomFile[machine]["taille_disque_dur"] = new_machine.taille_disque_dur
            listMachinesFomFile[machine]["os"] = new_machine.os
            listMachinesFomFile[machine]["version_os"] = new_machine.version_os
            bdd_file.write_bd(listMachinesFomFile)
            return "Vos informations ont bien été prise en compte.\n"
    return "Impossible de trouver le hostname de la machine.\n"


def delete_machine(hostname):
    """
        Methode permettant la suppression d'une machine à l'aide de son hostname
    :param hostname: nom de la machine
    :return:
    """
    for machine in range(len(listMachinesFomFile)):
        namehost = listMachinesFomFile[machine]["hostname"]
        if namehost == hostname:
            listMachinesFomFile.pop(machine)
            bdd_file.write_bd(listMachinesFomFile)
            return "La machine ayant le hostname " + hostname + " a été supprimée\n"
    return "Impossible de trouver le hostname de la machine\n"


def get_machines():
    """
        Methode qui va permettre de récupérer toutes les machines du parc informatique
    :return:
    """
    lstObjMachine = []
    for machine in listMachinesFomFile:
        instance_machine = Machine.Machine(machine["hostname"], machine["ip"], machine["nombre_cpu"],
                                           machine["taille_ram"], machine["nombre_disque_dur"],
                                           machine["taille_disque_dur"], machine["os"], machine["version_os"])
        lstObjMachine.append(instance_machine)
    return {"Liste listMachie": listMachinesFomFile}


def verif_insert_user():
    """
        Cette methode va permettre de vérifier les saisis utilisateurs
        on va vérfier s'il a bien saisi un nombre au lieu d'une lettre, s'il a bien respecté le nommage
        pour l'adresse ip etc...
    :return: on va retourner les saisis utilisateurs
    """
    lst_hostname = []
    lst_ip = []
    # initialize list hostname & list ip
    for i in listMachinesFomFile:
        lst_hostname.append(i["hostname"])
        lst_ip.append(i["ip"])
    hostnameFound = True  # initialize boolean for hostname
    while hostnameFound:
        hostname = input("Saisissez le hostname de la machine: ")
        if hostname in lst_hostname:
            print("Une machine possède déjà le hostname: " + hostname)
        else:
            hostnameFound = False
    IpOK = True  # initialize boolean for ip
    while IpOK:
        ip = input("Saisissez l'ip de la machine au format 127.0.0.1: ")
        if ip in lst_ip:
            print("Une machine possède déjà l'ip': " + ip)
        if verif_ip_valid(ip):
            IpOK = False
    isNumberCpu = True
    while isNumberCpu:
        cpu = input("Saisissez le nombre de cpu pour la machine: ")
        try:
            cpu = int(cpu)
            isNumberCpu = False
        except:
            print("La valeur du cpu saisie n'est pas un nombre")
    isNumberRam = True
    while isNumberRam:
        ram = input("Saisissez le nombre de ram pour la machine: ")
        try:
            ram = int(ram)
            isNumberRam = False
        except:
            print("La valeur de la Ram saisie n'est pas un nombre")
    isNumberDD = True
    while isNumberDD:
        numberDD = input("Saisissez le nombre de disque dur pour la machine: ")
        try:
            numberDD = int(numberDD)
            isNumberDD = False
        except:
            print("La valeur  saisie pour le nombre du disque dur n'est pas un nombre")
    isNumberSpaceDD = True
    while isNumberSpaceDD:
        spaceDD = input("Saisissez la taille du disque dur pour la machine: ")
        try:
            spaceDD = int(spaceDD)
            isNumberSpaceDD = False
        except:
            print("La valeur  saisie n'est pas un nombre")
    os = input("Saisissez l'os pour la machine: ")
    version_os = input("Saisissez la version de l'os pour la machine: ")
    return hostname, ip, cpu, ram, numberDD, spaceDD, os, version_os


def verif_ip_valid(ip):
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
