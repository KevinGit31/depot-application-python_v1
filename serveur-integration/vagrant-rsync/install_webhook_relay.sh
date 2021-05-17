#!/bin/bash

### MODE SECURE
set -u # en cas de variable non définit, arreter le script
set -e # en cas d'erreur (code de retour non-zero) arreter le script

### UTILITER ###
# fonctions, variables, etc.
# afin d'eviter les collisions, je vais préfixer mes fonction par ps_
# ps égale Poste

# Afficher de l'aide
ps_help(){
	1>&2 echo "Usage: ./script.sh DOMAIN"
	1>&2 echo ""
}

# Vérifier que le script est lancé en tant que root
ps_assert_root(){
	REAL_ID="$(id -u)"
	if [ "$REAL_ID" -ne 0 ]; then
		1>&2 echo "ERREUR: Le script doit etre exécuté en tant que root"
		exit 1
	fi
}

ps_install_webhook_relay(){
	wget -O /usr/local/bin/relay https://storage.googleapis.com/webhookrelay/downloads/relay-linux-amd64
	sudo chmod +wx /usr/local/bin/relay
	sudo relay login -k d8732914-8199-4198-a8c1-68be1cf8a290 -s Zu7hTxK9QwgN
	## export RELAY_KEY=d8732914-8199-4198-a8c1-68be1cf8a290
	## export RELAY_SECRET=Zu7hTxK9QwgN
	sleep 10s
}

### POINT D'ENTRER DU SCRIPT ###

## Vérifier que le script est lancé en tant que root
ps_assert_root

echo ""
echo "Please waiting for installation webhook relay"
ps_install_webhook_relay
relay forward --bucket github-jenkins http://172.30.1.3:8080/github-webhook/


