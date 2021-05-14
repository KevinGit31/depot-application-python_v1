#!/usr/bin/bash

### MODE SECURE
set -u # en cas de variable non définit, arreter le script
set -e # en cas d'erreur (code de retour non-zero) arreter le script

version=1.6

echo "$version"

curl -v --user admin:nexus_python --upload-file build/application-"$version".zip http://172.30.1.7:8081/repository/nexus-python/application-python/application-"$version".zip