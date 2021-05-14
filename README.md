# Sujet TP – Git, Python, API et Integration continue

**Ce document a pour but de guider et d'aider l'utilisateur à installer les différents environnements, exécuter les différents scripts.**


Pour Ce document va se présenter en 3 parties:

1. Installation du serveur d'application python
1. Installation du serveur jenkins
1. Installation du serveur nexus

## Données pac parc informatique
|Serveurs  | Noms Serveurs Vagrant |     @IP    | Port |
| ------------- |:-------------:|:-------------|-----------------------|
| serveur d'application python     | envdev    |   172.30.1.5/24            | |
| Serveur jenkins      | enjenkins     |   172.30.1.3/24            |  |
| Serveur nexus     | nexus     |      172.30.1.7/24        | |

##Architecture Applicatif du parc informatique

![Architecture Applicatif.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/develop/diagramme/Architecture_Applicatif.png "Diagramme.")

## Installation du serveur d'application python

Pour pouvoir installer le serveur applicatif, il vous faudra aller dans le 
répertoire /serveur-application/.

Une fois dans le répertoire, vous verrez un fichier VagrantFile

Il faudra ouvrir une "invite de commandes bash". Pour cela faite un clic droit avec 
votre souris et cliquer sur "Git bash here" (voir image).

**TODO Image**

Une fenêtre va alors s'ouvrir (voir image) 

**TODO Image**

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
> Installe Tous les composants nécessaires
> 
>> Python3 python3-dev python3-pip git, flask pytest, fastapi uvicorn
>

## Installation du serveur jenkins


Pour pouvoir installer le serveur applicatif, il vous faudra aller dans le 
répertoire /serveur-application/.

Une fois dans le répertoire, vous verrez un fichier VagrantFile

Il faudra ouvrir une "invite de commandes bash". Pour cela faite un clic droit avec 
votre souris et cliquer sur "Git bash here" (voir image).

**TODO Image**

Une fenêtre va alors s'ouvrir (voir image) 

**TODO Image**

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
> Installe Tous les composants nécessaires
> 
>> Python3 python3-dev python3-pip git, flask pytest, fastapi uvicorn
>

## Installation du serveur nexus


Pour pouvoir installer le serveur applicatif, il vous faudra aller dans le 
répertoire /serveur-application/.

Une fois dans le répertoire, vous verrez un fichier VagrantFile

Il faudra ouvrir une "invite de commandes bash". Pour cela faite un clic droit avec 
votre souris et cliquer sur "Git bash here" (voir image).

**TODO Image**

Une fenêtre va alors s'ouvrir (voir image) 

**TODO Image**

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
> Installe Tous les composants nécessaires
> 
>> nexus
>