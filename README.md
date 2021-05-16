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

## Installation des Pré-requis

**Vérifier l'installation de git**

* Ouvrir une invite de commande cmd sous Windows et taper la commande suivante (voir image) 
```
git --version
```
![CMD.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/cmd.PNG "Diagramme.")

* Si pas d'install git, suivre le lien 
[d'installation de Git](https://git-scm.com/downloads).

**Une fois l'installation de git faite**

* Créez un dossier sous Windows
* Allez dans le dossier
* Ouvrir une "invite de commandes bash". Pour cela faite un clic droit avec 
votre souris et cliquer sur "Git bash here" (voir image).

![invite bash.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/invit-bash.PNG "Diagramme.")

Une fenêtre va alors s'ouvrir (voir image) 

![Fenêtre.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash.PNG "Diagramme.")

* Faire un git clone de notre depot git en tapant la commande suivante
```
git clone https://github.com/KevinGit31/depot-application-python_v1.git
```

**Vous êtes prêt à tester notre application**



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
>>  Active le port 8000 


#### Test Application python avec l'API FastApi


Pour pouvoir tester l'application avec FastApi, il va vous falloir un Environnement de développement (IED) de votre choix qui peut exécuter du code python. Quelques exemples (Visual studio code, PyCharm).

Si vous n'avez pas d'IDE, suivre le lien d'installation de votre choix

* Lien
[d'installation visual studio code](https://code.visualstudio.com/download).
* Lien
[d'installation de pyCharm](https://www.jetbrains.com/fr-fr/pycharm/).

Une fois votre IDE installé, ouvrer le et importer le projet python qui se trouve
dans le répertoire /application/src/.

* Importer le projet sur Visual studio code (VSC)

Une fois sur VSC, faire un clic sur ***File*** puis ***Open Folder*** et ouvrer le 
dossier /application/. (voir image).

![vsc import.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/vsc-import.png "Diagramme.")

**Exécution de l'application python** 

Ouvrer le fichier ***mainFastApi.py*** et cliquer sur le bouton **1** (voir image).

![vsc run.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/vsc-run.png "Diagramme.")

**l'Application est prête à être testé**

* Importer le projet sur PyCharm

TODO

**Nous allons tester notre application sur Postman**

Si Postman n'est pas encore installé, suivre le lien [d'installation](https://www.postman.com/downloads/).

Ouvrir Postman une fois installé et cliquer ***My Workspace*** puis sur ***Collections*** => ***Import*** => ***File*** => ***Upload Files***

Importer le fichier ***App-Python-API.postman_collection.json*** qui se trouve dans
le repètoire /depot-application-python_v1/ (voir image)

![import postman.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Postman.PNG "Diagramme.")

Test API Get All machines

![get machines.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/getMachines.PNG "Diagramme.")

Test API Get machine by hostname

![Get machine by hostname.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/getMachineByHostname.PNG "Diagramme.")

Test API Update machine by hostname

![Update machine by hostname.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/updateMachineByHostname.PNG "Diagramme.")

Test API Delete machine by hostname

![Delete machine by hostname.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/deleteMachineByHostname.PNG "Diagramme.")

Test API Create machine

![Create machine.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/createMachine.PNG "Diagramme.")


* Documentation Swagger API

L'application étant toujours démarrée sur VSC ou PyCharm, cliquer sur ce lien [documentation 
applicaton python](http://127.0.0.1:8000/docs) pour acceder à Swagger API (voir image) 

TODO image



## Installation du serveur jenkins

Pour pouvoir installer le serveur applicatif, il vous faudra aller dans le 
répertoire /serveur-integration/.

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
> création d'un utilisateur userjob
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
répertoire /serveur-nexus/.

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