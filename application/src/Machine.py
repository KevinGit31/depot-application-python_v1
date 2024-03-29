from pydantic import BaseModel
from typing import Optional


class Machine:
    def __init__(self, hostname, ip, nombre_cpu, taille_ram, nombre_disque_dur, taille_disque_dur, os, version_os):
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


class MachineFastApi(BaseModel):
    hostname: str
    ip: str
    nombre_cpu: int
    taille_ram: int
    nombre_disque_dur: int
    taille_disque_dur: int
    os: str
    version_os: str