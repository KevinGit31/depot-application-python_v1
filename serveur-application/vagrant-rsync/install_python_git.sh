#!/usr/bin/env bash

### MODE SECURE
set -u # en cas de variable non définit, arreter le script
set -e # en cas d'erreur (code de retour non-zero) arreter le script

# Vérifier que le script est lancé en tant que root
ps_assert_root(){
	REAL_ID="$(id -u)"
	if [ "$REAL_ID" -ne 0 ]; then
		1>&2 echo "ERREUR: Le script doit etre exécuté en tant que root"
		exit 1
	fi
}

ps_assert_root

apt update -y

# install python
apt install python3 python3-dev python3-pip git -q -y
apt remove -y python 

# positionnement de python3 et pip3 dans le profil
ps_verif_dossier_pyhton() {
    
    if [ -f "/usr/bin/python" ] ; then
        echo "file exist"
    else
        ln -s /usr/bin/python3 /usr/bin/python
    fi
}
ps_verif_dossier_pyhton
echo "alias pip=pip3" > ~/.bashrc
#install utilitaire de test dont flask et fastapi pour expostion de l'api
pip install flask pytest 
pip install fastapi uvicorn

sudo apt install ufw

	#Activer ufw
	echo y | sudo ufw enable
	if [ $? -gt 0 ]; then
		echo "Erreur lors de l'activation de UFW"
		exit 1;
	fi

	#Ouverture du port 8000
	sudo ufw allow 8000

	# Verification de l'ouverture des ports
	sudo ufw status numbered

echo "Success"
