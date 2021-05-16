#!/usr/bin/bash

### MODE SECURE
set -u # en cas de variable non définit, arreter le script
set -e # en cas d'erreur (code de retour non-zero) arreter le script

git add script.sh
git add gradle.properties

git commit -m "update gradle properties & script sh"

git push origin develop

echo "Success"