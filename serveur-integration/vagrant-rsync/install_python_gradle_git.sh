#!/usr/bin/env bash

VERSION=7.0

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

apt update

apt install -y unzip
 
# install python
apt install python3 python3-dev python3-pip git -q -y

## Récupération de la dernière version

wget https://services.gradle.org/distributions/gradle-${VERSION}-bin.zip -P /tmp

unzip -d /opt/gradle /tmp/gradle-${VERSION}-bin.zip

# Faire pointer le lien vers la dernière version de gradle

ln -s /opt/gradle/gradle-${VERSION} /opt/gradle/latest

# Ajout de gradle au PATH

touch /etc/profile.d/gradle.sh

echo "export PATH=/opt/gradle/latest/bin:${PATH}" > /etc/profile.d/gradle.sh

chmod +x /etc/profile.d/gradle.sh

source /etc/profile.d/gradle.sh

echo "Success"
