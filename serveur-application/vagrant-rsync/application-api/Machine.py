from pydantic import BaseModel
from typing import Optional


class MachineFastApi(BaseModel):
    hostname: str
    ip: str
    nombre_cpu: int
    taille_ram: int
    nombre_disque_dur: int
    taille_disque_dur: int
    os: str
    version_os: str



