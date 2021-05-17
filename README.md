# Sujet TP – Git, Python, API et Integration continue

**Ce document a pour but de guider et d'aider l'utilisateur à installer les différents environnements,et exécuter les différents scripts.**

## Organisation du projet

Pour pouvoir mener à bien ce projet, le premier jour, nous avons recueilli les besoins du client que nous 
avons transformés en user story. Toutes ces stories, nous les avons mises sur notre trello. Chaque story a été 
découpée en petite tâche par la suite. Dans la continuité, une fois toutes les tâches recensées, nous avons 
commencé à mettre en place les différents environnements (intégration, nexus, application). Après développement des
 environnements, nous avons créé notre première pull request pour pouvoir faire une review et tester 
 aussi les différents environnement développés. Suite à la mise en place de ces environnements, nous avons commencé
 à développer deux applications python, l'une sur la partie console et l'autre sur la partie fastApi (équivalent à l'outil de développement flask) 
 sur des branches distinctes. Une fois les développements faits, nous avons réalisé des reviews de codes en faisant des pull requests.
 Nous nous sommes organisés afin de réaliser des points d'avancement réguliers, en matinée et en après-midi.


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


Notre chaine d'intégration continue va fonctionner selon l'architecture applicative ci-dessus. Nous avons nos postes en local où le développeur développe
son application, puis il pousse son code petit à petit sur le repository Git. A chaque push sur une 
branch ou le merge d'une branch dans une autre, il y aura un build qui va être lancé sur notre serveur 
d'intégration qui va builder notre application au format zip et le pousser sur notre repos Nexus. 
Pour permettre un build Jenkins à chaque push ou à chaque merge sur une branch git, nous avons mis en place un webhook relay.
Voici les différentes instructions pour pouvoir mettre en place le webhook_relay :
- https://webhookrelay.com/blog/2017/11/23/github-jenkins-guide/#Step-2-Jenkins-Installation-if-you-already-have-it-ignore-this-step)
- https://webhookrelay.com/v1/installation/cli)

Mise en place du webhool_relay sur notre projet Git (voir image suivante)

![Git_webhook_relay_v1.PNG](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Git_webhook_relay_v1.PNG "Git_webhook_relay_v1")

Dans la partie Payload URL, nous avons l'url fournie par webhook relay qui est installée sur notre serveur jenkins, et nous l'avons configurée
 pour qu'un build Jenkins soit déclenché à chaque push.


![Git_webhook_relay_v2](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Git_webhook_relay_v2.PNG "Git_webhook_relay_v2")

Côté Jenkins, nous avons lancé la commande suivante:
````
sudo relay forward --bucket github-jenkins http://172.30.1.3:8080/github-webhook/
````
Cette commande va permettre de lier notre repos git à notre serveur d'intégration jenkins, et il nous fournit le lien à mettre dans le payload url de git

![Git_webhook_relay_v3](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Git_webhook_relay_v3.PNG "Git_webhook_relay_v3")

La configuration du job jenkins se trouve à la racine du répertoire du nom de "configJobJenkins.xml".
Côté jenkins, nous avons configuré un job, nous lui avons renseigné notre repos Git, ainsi que la branche sur laquelle, il fera un checkout.
Pour déclencher le build du job, nous avons coché l'option "Github hook trigger for gitscm polling".
![Jenkins_v1](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Jenkins_v1.PNG "Jenkins_v1")
![Jenkins_v1](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Jenkins_v2.PNG "Jenkins_v1")
![Jenkins_v1](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Jenkins_v3.PNG "Jenkins_v1")

Une fois, que jenkins est configurée et qu'un push ou un merge a été fait,nous constatons ainsi que le git a bien lancé le build.

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

**Une fois l'installation de git réalisée**

* Créez un dossier sous Windows
* Allez dans le dossier
* Ouvrez une "invite de commandes bash". Pour cela, faites un clic droit avec votre souris et cliquez sur "Git bash here" (voir image).

![invite bash.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/invit-bash.PNG "Diagramme.")

Une fenêtre va alors s'ouvrir (voir image) 

![Fenêtre.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash.PNG "Diagramme.")

* Faites un git clone du repos git en tapant la commande suivante
```
git clone https://github.com/KevinGit31/depot-application-python_v1.git
```




## Installation du serveur d'application python

Pour pouvoir installer le serveur applicatif, il vous faudra aller dans le répertoire /serveur-application/.

Une fois dans le répertoire, vous verrez un fichier VagrantFile.

Il faudra ouvrir une "invite de commandes bash". Pour cela, faites un clic droit avec votre souris et cliquez sur "Git bash here" (voir image).

![invite bash.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/invit-bash.PNG "Diagramme.")

Une fenêtre va alors s'ouvrir (voir image) 

![Fenêtre.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash.PNG "Diagramme.")

Tapez la commande suivante :
```
vagrant up
```
Elle a pour but de lancer le script qui permet la création de la machine virtuelle.

Une fois la création de la machine virtuelle faite, tapez la commande :
```
vagrant ssh
```
pour entrer dans votre machine.

Une fois dans la machine, tapez la commande suivante :
```
cd /home/rsync
```
Dans le dossier /home/rsync, tapez la commande suivante :
```
sudo apt install dos2unix
```
Une fois l'installation faite, tapez la commande suivante :
```
dos2unix install_python_git.sh
```
Elle a pour but de convertir install_python_git.sh au fomat unix.

Pour lancer le script, tapez la commande suivante :
```
sudo ./install_python_git.sh
```
>  Elle installe tous les composants nécessaires à l'utilisation des outils de développement suivants :
> 
>> Python3, python3-dev, python3-pip git, flask pytest, fastapi, uvicorn
>
> Elle installe également UFW pour la confiration du pare-feu
> 
>> Et active le port 8000 


###  Installation et fonctionnement de l'application console et API

Notre application python se découpe en deux applications, une application qui s'exécute sur la console et une autre qui va s'exécuter via le serveur fastApi.
L'application python se trouvera dans un fichier zip ( ex: application-1.7.zip) qui se trouve à la racine du projet dont vous avez  fait le "clone" auparavant.

L'application va permettre à l'utilisateur de réaliser les actions suivantes :
- Lister les machines présentes sous son parc informatique
- Afficher les détails d'une machine en saisissant son "hostname"
- Ajouter une nouvelle machine dans son parc informatique en saisissant les informations qu'il faut
- Supprimer une machine existante en saisissant son "hostname"
- Modifier les caractéristiques d'une machine en saisissant son "hostname"
- Lister toutes les applications qui sont disponibles sur notre nexus repository,si nexus est disponible (une capture d'écran du nexus en marche)

Mettez-vous dans le repertoire suivant "depot-application-python_v1" puis faites un clic droit et cliquez sur "git bash here".

![Project_directory.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/reamde_part2/diagramme/Project_directory.PNG "Project_directory.PNG")

![invite bash.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/invit-bash.PNG "Diagramme.")

Alors une fenêtre bash va s'ouvrir.

![fenetre-project.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/reamde_part2/diagramme/fenetre-project.PNG "fenetre-project.PNG")

Tapez les commandes suivantes pour pouvoir installer l'application sur le serveur d'application.
````
cp application-1.7.zip serveur-application/vagrant-rsync/
````
Copiez l'application zip dans le répertoire serveur-application/vagrant-rsync/
````
cd serveur-application/vagrant-rsync/
````
Déplacez vous dans le répertoire 
````
unzip application-1.7.zip
````
Dézippez votre fichier

Maintenant que l'application est installée, vous allez vous rendre sur le serveur d'application. Pour cela, tapez les commandes suivantes:
````
vagrant up
````
Cette commande vous permet de lancer le serveur.
````
vagrant ssh
````
Cette commande a pour but de vous connecter au serveur d'application.
````
cd /home/rsync/
````
Cette commande vous amène dans le répertoire où l'application a été installée.

**Test Application python avec la console**

Une fois dans le répertoire /home/rsync/, lancez l'application console python, en tapant la commande suivante:
````
python main.py
````
![Application console.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash-application-console-repos.PNG "Application console.")


![Application console.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash-application-console-repos.PNG "fenetre-bash-application-console-repos")


**Test Application python avec l'API FastApi**

Pour pouvoir tester l'application avec FastApi, il va vous falloir un environnement de développement (IED) de votre choix qui peut exécuter du code python, exemples : (Visual studio code, PyCharm).

Si vous n'avez pas d'IDE, suivez le lien d'installation de votre choix :

* Lien
[d'installation de visual studio code](https://code.visualstudio.com/download).
* Lien
[d'installation de pyCharm](https://www.jetbrains.com/fr-fr/pycharm/).

Une fois votre IDE installé, ouvrez le et importez le projet python qui se trouve dans le répertoire /serveur-application/vagrant-rsync/.

* Importer le projet sur Visual studio code (VSC)

Une fois sur VSC, faites un clic sur ***File*** puis ***Open Folder*** et ouvrez le dossier /serveur-application/vagrant-rsync/. (voir image).

![vsc import.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/vsc-import.png "Diagramme.")

**Exécution de l'application python** 

Ouvrez le fichier ***mainFastApi.py*** et cliquez sur le bouton **1** (voir image).

![vsc run.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/vsc-run.png "Diagramme.")

**l'Application est prête à être testée**

* Importer le projet sur PyCharm

TODO

**Nous allons tester notre application sur Postman**

Si Postman n'est pas encore installé, suivez le lien [d'installation](https://www.postman.com/downloads/).

Ouvrez Postman une fois installé, cliquez ***My Workspace*** puis sur ***Collections*** => ***Import*** => ***File*** => ***Upload Files***

Importez le fichier ***App-Python-API.postman_collection.json*** qui se trouve dans le repètoire /depot-application-python_v1/ (voir image)

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

L'application étant toujours démarrée sur VSC ou PyCharm, cliquez sur ce lien [documentation applicaton python](http://127.0.0.1:8000/docs) pour accéder à Swagger API (voir image) 

![Swagger API.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/Swagger.PNG "Diagramme.")



## Installation du serveur jenkins

Pour pouvoir installer le serveur applicatif, il vous faudra aller dans le répertoire /serveur-integration/.

Dans le répertoire, vous verrez un fichier VagrantFile. Il faudra ouvrir une "invite de commandes bash", pour cela faites un clic droit avec 
votre souris et cliquez sur "Git bash here" (voir image).

![invite bash.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/invit-bash.PNG "Diagramme.")

Une fenêtre va alors s'ouvrir (voir image) 

![Fenêtre.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash.PNG "Diagramme.")

Tapez la commande suivante :
```
vagrant up
```
Elle a pour but de lancer le script qui permet la création de la machine virtuelle.

Une fois la création de la machine virtuelle faite, taper la commande
```
vagrant ssh
```
pour entrer dans votre machine.

Dans la machine tapez la commande suivante
```
cd /home/rsync
```
Dans le dossier /home/rsync, tapez la commande suivante
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

Tapez la commande suivante pour lancer le script
```
sudo ./provision.sh
```
> Elle installe la version stable de jenkins et tous les composants nécessaires aux outils de développement suivants :
> 
>> gnupg, gnupg2, gnupg1, openjdk-11-jdk et jenkins
>
> Elle permet la création d'un utilisateur userjob
>
>> pour donner les droits apt au userjob
>
> Elle affiche à la fin de l'exécution du script le mot de passe Jenkins
>>sudo cat /var/lib/jenkins/secrets/initialAdminPassword
>
> Elle installe UFW pour la confiration du pare-feu
> 
>>  Et active les ports 8080 et OpenSSH 


Tapez la commande suivante pour lancer le script 
```
sudo ./install_webhook_relay.sh
```

> Installe le Webhook Relay
> 


Tapez la commande suivante pour lancer le script
```
sudo install_python_gradle_git.sh 
```
> Installe tous les composants nécessaires 
> 
>> unzip, python3, python3-dev, python3-pip, git et gradle
>



## Installation du serveur nexus

Pour pouvoir installer le serveur applicatif, il vous faudra aller dans le répertoire /serveur-nexus/.

Une fois dans le répertoire, vous verrez un fichier VagrantFile

Il faudra ouvrir une "invite de commandes bash". Pour cela faites un clic droit avec votre souris et cliquez sur "Git bash here" (voir image).

![invite bash.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/invit-bash.PNG "Diagramme.")

Une fenêtre va alors s'ouvrir (voir image) 

![Fenêtre.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash.PNG "Diagramme.")

Taper la commande suivante :
```
vagrant up
```
Elle a pour but de lancer le script qui permet la création de la machine virtuelle.

Une fois la création de la machine virtuelle faite, taper la commande
```
vagrant ssh
```
Pour entrer dans votre machine

Une fois dans la machine tapez la commande suivante
```
cd /home/rsync
```
Dans le dossier /home/rsync, tapez la commande suivante
```
sudo apt install dos2unix
```
Une fois l'installation faite, tapez la commande suivante
```
dos2unix install_nexus.sh
```
Elle a pour but de convertir install_nexus.sh au fomat unix

Tapez la commande suivante pour lancer le script
```
sudo ./install_nexus.sh
```
> Installe penjdk-8-jdk et nexus
>
> Installe UFW pour la confiration du pare-feu
> 
>> Active les ports 8080 et OpenSSH 