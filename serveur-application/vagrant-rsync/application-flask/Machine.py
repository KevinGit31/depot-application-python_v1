class Machine:
    
    def __init__(self, id, hostname, ip, nombre_cpu, taille_ram, nombre_disque_dur, taille_disque_dur, os, version_os):
        self._id = id
        self._hostname = hostname
        self._ip = ip
        self._nombre_cpu = nombre_cpu
        self._taille_ram = taille_ram
        self._nombre_disque_dur = nombre_disque_dur
        self._taille_disque_dur = taille_disque_dur
        self._os = os
        self._version_os = version_os

    @property
    def id(self):
        return self._id

    @property
    def hostname(self):
        return self._hostname

    @property
    def ip(self):
        return self._ip

    @property
    def nombre_cpu(self):
        return self._nombre_cpu

    @property
    def taille_ram(self):
        return self._taille_ram

    @property
    def nombre_disque_dur(self):
        return self._nombre_disque_dur

    @property
    def taille_disque_dur(self):
        return self._taille_disque_dur

    @property
    def os(self):
        return self._os

    @property
    def version_os(self):
        return self._version_os
