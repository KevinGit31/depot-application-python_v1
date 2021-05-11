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
        
        #super().__init__()


