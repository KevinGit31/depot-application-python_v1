# Sujet TP – Git, Python, API et Integration continue

**Ce document a pour but de guider et d'aider l'utilisateur à installer les différents environnements, exécuter les différents scripts.**


Le document va se présenter en 3 parties:

1. Installation du serveur d'application python
1. Installation du serveur jenkins
1. Installation du serveur nexus

## Données parc informatique
|Serveurs  | Noms Serveurs Vagrant |     @IP    | Port |
| ------------- |:-------------:|:-------------|-----------------------|
| serveur d'application python     | envdev    |   172.30.1.5/24            | |
| Serveur jenkins      | enjenkins     |   172.30.1.3/24            |  |
| Serveur nexus     | nexus     |      172.30.1.7/24        | |


## Architecture Applicative

![Architecture Applicative.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Architecture_Applicative.png "Diagramme.")

## Diagramme UML

![Diagramme UML.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Diagramme_Classe.png "Diagramme.")

## Installation du serveur d'application python

Pour pouvoir installer le serveur applicatif, il vous faudra aller dans le 
répertoire /serveur-application/.

Une fois dans le répertoire, vous verrez un fichier VagrantFile

Il faudra ouvrir une "invite de commandes bash". Pour cela faite un clic droit avec 
votre souris et cliquer sur "Git bash here" (voir image).

![invite bash.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/invit-bash.PNG "Diagramme.")

Une fenêtre va alors s'ouvrir (voir image) 

![Fenêtre.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash.PNG "Diagramme.")

Taper la commande suivante :
```
vagrant up
```
Elle a pour but de lancer le script qui permet la création de la machine virtuel.

Une fois la création de la machine virtuel faite, taper la commande
```
vagrant ssh
```
Pour entrer dans votre machine

Une fois dans la machine tapez la commande suivante
```
cd /home/rsync
```
Une fois dans le dossier /home/rsync, tapez la commande suivante
```
sudo apt install dos2unix
```
Une fois l'installation faite, tapez la commande suivante
```
dos2unix install_python_git.sh
```
Elle a pour but de convertir install_python_git.sh au fomat unix

Tapez la commande suivante pour lancer le script et valider
```
sudo ./install_python_git.sh
```
> Installe tous les composants nécessaires
> 
>> Python3 python3-dev python3-pip git, flask pytest, fastapi, uvicorn
>
> Installe UFW pour la confiration du pare-feu
> 
>>  Active les ports 8000 et OpenSSH 

## Installation du serveur jenkins

Pour pouvoir installer le serveur applicatif, il vous faudra aller dans le 
répertoire /serveur-application/.

Une fois dans le répertoire, vous verrez un fichier VagrantFile

Il faudra ouvrir une "invite de commandes bash". Pour cela faite un clic droit avec 
votre souris et cliquer sur "Git bash here" (voir image).

![invite bash.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/invit-bash.PNG "Diagramme.")

Une fenêtre va alors s'ouvrir (voir image) 

![Fenêtre.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash.PNG "Diagramme.")

Taper la commande suivante :
```
vagrant up
```
Elle a pour but de lancer le script qui permet la création de la machine virtuel.

Une fois la création de la machine virtuel faite, taper la commande
```
vagrant ssh
```
Pour entrer dans votre machine

Une fois dans la machine tapez la commande suivante
```
cd /home/rsync
```
Une fois dans le dossier /home/rsync, tapez la commande suivante
```
sudo apt install dos2unix
```
Une fois l'installation faite, tapez les commandes suivantes
```
dos2unix provision.sh
```
Elle a pour but de convertir provision.sh au fomat unix
```
dos2unix install_python_gradle_git.sh
```
Elle a pour but de convertir install_python_gradle_git.sh au fomat unix

Tapez la commande suivante pour lancer le script et valider
```
sudo ./provision.sh
```
> Installe la version stable de jenkins et tous les composants nécessaires 
> 
>> gnupg, gnupg2, gnupg1, openjdk-11-jdk et jenkins
>
> Créer un utilisateur userjob
>
>>Donne les droits apt au userjob
>
>Affiche à la fin de l'exécution du script le mot de passe Jenkins
>>sudo cat /var/lib/jenkins/secrets/initialAdminPassword
>
> Installe UFW pour la confiration du pare-feu
> 
>>  Active les ports 8080 et OpenSSH 

Tapez la commande suivante pour lancer le script et valider
```
sudo install_python_gradle_git.sh
```
> Installe tous les composants nécessaires 
> 
>> unzip, python3, python3-dev, python3-pip, git et gradle
>



## Installation du serveur nexus

Pour pouvoir installer le serveur applicatif, il vous faudra aller dans le 
répertoire /serveur-application/.

Une fois dans le répertoire, vous verrez un fichier VagrantFile

Il faudra ouvrir une "invite de commandes bash". Pour cela faite un clic droit avec 
votre souris et cliquer sur "Git bash here" (voir image).

![invite bash.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/invit-bash.PNG "Diagramme.")

Une fenêtre va alors s'ouvrir (voir image) 

![Fenêtre.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash.PNG "Diagramme.")

Taper la commande suivante :
```
vagrant up
```
Elle a pour but de lancer le script qui permet la création de la machine virtuel.

Une fois la création de la machine virtuel faite, taper la commande
```
vagrant ssh
```
Pour entrer dans votre machine

Une fois dans la machine tapez la commande suivante
```
cd /home/rsync
```
Une fois dans le dossier /home/rsync, tapez la commande suivante
```
sudo apt install dos2unix
```
Une fois l'installation faite, tapez la commande suivante
```
dos2unix install_nexus.sh
```
Elle a pour but de convertir install_nexus.sh au fomat unix

Tapez la commande suivante pour lancer le script et valider
```
sudo ./install_nexus.sh
```
> Installe tous les composants nécessaires
> 
>> penjdk-8-jdk, nexus
>
> Installe UFW pour la confiration du pare-feu
> 
>>  Active les ports 8080 et OpenSSH 