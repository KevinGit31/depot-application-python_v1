# Sujet TP – Git, Python, API et Integration continue

**Ce document a pour but de guider et d'aider l'utilisateur à installer les différents environnements, exécuter les différents scripts.**

## Organisation du projet

Pour pouvoir mener à bien ce projet, le premier jour nous avons recueilli les besoins du client que nous avons transformé en story. Toutes ces stories, nous les avons mises sur notre trello. Chaque story a été découpée en petite tâche par la suite. Dans la continuité, une fois toutes les tâches recensées, nous avons commencé à mettre en place les différents environnement (intégration, nexus, application), une fois les environnement développé on a crée notre première pull request pour pouvoir faire une review et testé aussi les différents environnement développés. Une fois les environnements mis en place, nous avons commencé à développer l'application python un sur la partie console et un autre sur la partie fastApi (equivaut à flask aussi) sur des branches distincts. Une fois les dev faits, on faisait des pull request et l'un faisait la review de l'autre pour comprendre son code mais aussi vérifier si tous les tests ont été. Et chaque matin on se faisait des points pour savoir sur quelle tâche nous allons partir et si on a des blocages, ainsi qu'un point dans l'après midi pour se synchroniser.


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


## Comment fonctionne notre chaine d'intégration

### Architecture Applicative

![Architecture Applicative.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Architecture_Applicative.png "Diagramme.")


Voilà comment notre chaine d'intégration continue va fonctionner. Nous avons nos postes local où le développeur développe
son application, puis il va pousser son code petit à petit sur le repot Git. A chaque push sur une branch ou le merge d'une branch dans une autre il y aura un build qui va être lancé sur notre serveur d'intégration qui va builder notre application au format zip et le pousser sur notre repos Nexus. Pour permettre un build Jenkins à chaque push ou merge sur une branch git, nous avons mis en place un webhook relay.
Voici les différentes instructions pour pouvoir mettre en place le webhook_relay :
- https://webhookrelay.com/blog/2017/11/23/github-jenkins-guide/#Step-2-Jenkins-Installation-if-you-already-have-it-ignore-this-step)
- https://webhookrelay.com/v1/installation/cli)

Mise en place du webhool_relay sur notre projet Git (voir image suivante)

![Git_webhook_relay_v1.PNG](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Git_webhook_relay_v1.PNG "Git_webhook_relay_v1")

Dans la partie Payload URL, nous avons l'url fourni par webhook relay qui est installé sur notre serveur jenkins, et on l'a configuré pour chaque push il va déclencher un build sur Jenkins

![Git_webhook_relay_v2](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Git_webhook_relay_v2.PNG "Git_webhook_relay_v2")

Côté Jenkins nous avons lancé la commande suivante:
````
sudo relay forward --bucket github-jenkins http://172.30.1.3:8080/github-webhook/
````
Cette commande va permettre de lié notre répos git à notre serveur d'intégration jenkins, et il nous fournit le lien à mettre dans le payload url de git

![Git_webhook_relay_v3](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Git_webhook_relay_v3.PNG "Git_webhook_relay_v3")

La configuration du job jenkins se trouve à la racine du répertoire du nom de "configJobJenkins.xml".
Côté jenkins, nous avons configuré un job, nous lui avons renseigné notre repos Git, ainsi que la branche sur lequel il fera un checkout, comment le build du job va être déclenché on a coché l'option "Github hook trigger for gitscm polling"
![Jenkins_v1](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Jenkins_v1.PNG "Jenkins_v1")
![Jenkins_v1](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Jenkins_v2.PNG "Jenkins_v1")
![Jenkins_v1](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Jenkins_v3.PNG "Jenkins_v1")

Une fois la configuration du jenkins faite, et qu'on fait un push sur notre projet on constate que le git a bien lancé le build.

![Jenkins_build_auto](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Jenkins_build_auto.PNG "Jenkins_build_auto")



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


###  Installation et fonctionnement de l'application console et API

Notre application python se découpe en deux applications une première application qui s'exécute sur la console et une autre qui va s'exécuter via le serveur "fastApi".
L'application python se trouvera dans un fichier zip ( ex: application-1.7.zip) qui se trouve à la racine du projet que vous avez "clone" auparavant.

L'application fonctionne de la manière suivante:
- Elle va permettre à l'utilisateur de lister les machines présentes sous son parc informatique
- Elle va permettre à l'utilisateur de d'afficher les détails d'une machine en saisissant son "hostname"
- Elle va permettre d'ajouter une nouvelle machine dans son parc informatique en saisissant les informations qu'il faut
- Elle va permettre de supprimer une machine existante en saisissant son "hostname"
- Elle va permettre de modifier les caractéristiques d'une machines en saisissant son "hostname"
- Elle va permettre aussi de lister toutes les applications qui sont disponibles sur notre nexus repository (si nexus disponible, une capture d'écran avec le nexus up)

Mettez-vous dans le repertoire suivant "depot-application-python_v1" puis faite un clique droit et cliquer sur "git bash here.

![Project_directory.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/reamde_part2/diagramme/Project_directory.PNG "Project_directory.PNG")

![invite bash.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/invit-bash.PNG "Diagramme.")

Alors une fenêtre bash va s'ouvrir.

![fenetre-project.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/reamde_part2/diagramme/fenetre-project.PNG "fenetre-project.PNG")

Tapez les commandes suivantes pour pouvoir installer l'application sur le serveur d'application.
````
cp application-1.7.zip serveur-application/vagrant-rsync/
````
nous allons copier l'application zip dans le répertoire serveur-application/vagrant-rsync/
````
cd serveur-application/vagrant-rsync/
````
On va se deplacer dans le répertoire 
````
unzip application-1.7.zip
````
on va dézipper notre fichier

Maintenant que l'application est installée, nous allons nous rendre sur le serveur d'application. Pour cela nous allons taper les commandes suivantes:
````
vagrant up
````
Cette commande a pour but de lancer le serveur
````
vagrant ssh
````
Cette commande a pour but de se connecter à notre serveur d'application
````
cd /home/rsync/
````
Cette commande a pour but de nous amener dans le répertoire où notre application a été installé.

**Test Application python avec la console**

Une fois dans le répertoire /home/rsync/, nous allons lancer notre application console python, pour cela on va lancer la commande suivante:
````
python main.py
````
![Application console.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash-application-console-repos.PNG "Application console.")


![Application console.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash-application-console-repos.PNG "fenetre-bash-application-console-repos")


**Test Application python avec l'API FastApi**

Pour pouvoir tester l'application avec FastApi, il va vous falloir un Environnement de développement (IED) de votre choix qui peut exécuter du code python. Quelques exemples (Visual studio code, PyCharm).

Si vous n'avez pas d'IDE, suivre le lien d'installation de votre choix

* Lien
[d'installation de visual studio code](https://code.visualstudio.com/download).
* Lien
[d'installation de pyCharm](https://www.jetbrains.com/fr-fr/pycharm/).

Une fois votre IDE installé, ouvrer le et importer le projet python qui se trouve
dans le répertoire /serveur-application/vagrant-rsync/.

* Importer le projet sur Visual studio code (VSC)

Une fois sur VSC, faire un clic sur ***File*** puis ***Open Folder*** et ouvrer le 
dossier /serveur-application/vagrant-rsync/. (voir image).

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

![Swagger API.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Swagger.PNG "Diagramme.")



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
dos2unix install_webhook_relay.sh
```
Elle a pour but de convertir install_webhook_relay.sh au fomat unix
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
sudo ./install_webhook_relay.sh
```

> Installe tous les composants nécessaires 
> 
>> Webhook Relay
>

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