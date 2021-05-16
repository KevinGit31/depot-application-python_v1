## Installation et fonctionnement de l'application console

Notre application python se découpe en deux applications une première application qui s'exécute sur la console et une autre qui va s'exécuter via le serveur "fastApi".
L'application python se trouvera dans un fichier zip ( ex: application-1.7.zip) qui se trouve à la racine du projet que vous avez "clone" auparavant.

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
Cette commande a pour but de se connecter à notre serveur d'application (image)
````
cd /home/rsync/
````
Cette commande a pour but de nous amener dans le répertoire où notre application a été installé.

Une fois dans le répertoire /home/rsync/, nous allons lancer notre application console python, pour cela on va lancer la commande suivante:
````
python main.py
````
![Application console.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash-application-console-repos.PNG "Application console.")

L'application fonctionne de la manière suivante:
- Elle va permettre à l'utilisateur de lister les machines présentes sous son parc informatique
- Elle va permettre à l'utilisateur de d'afficher les détails d'une machine en saisissant son "hostname"
- Elle va permettre d'ajouter une nouvelle machine dans son parc informatique en saisissant les informations qu'il faut
- Elle va permettre de supprimer une machine existante en saisissant son "hostname"
- Elle va permettre de modifier les caractéristiques d'une machines en saisissant son "hostname"
- Elle va permettre aussi de lister toutes les applications qui sont disponibles sur notre nexus repository (si nexus disponible, une capture d'écran avec le nexus up) ![Application console.](https://raw.githubusercontent.com/KevinGit31/depot-application-python_v1/readme/diagramme/fenetre-bash-application-console-repos.PNG "fenetre-bash-application-console-repos")


## Comment fonctionne notre chaine d'intégration
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


## Organisation du projet

Pour pouvoir mener à bien ce projet, le premier jour nous avons recueilli les besoins du client que nous avons transformé en story. Toutes ces stories, nous les avons mises sur notre trello. Chaque story a été découpée en petite tâche par la suite. Dans la continuité, une fois toutes les tâches recensées, nous avons commencé à mettre en place les différents environnement (intégration, nexus, application), une fois les environnement développé on a crée notre première pull request pour pouvoir faire une review et testé aussi les différents environnement développés. Une fois les environnements mis en place, nous avons commencé à développer l'application python un sur la partie console et un autre sur la partie fastApi (equivaut à flask aussi) sur des branches distincts. Une fois les dev faits, on faisait des pull request et l'un faisait la review de l'autre pour comprendre son code mais aussi vérifier si tous les tests ont été. Et chaque matin on se faisait des points pour savoir sur quelle tâche nous allons partir et si on a des blocages, ainsi qu'un point dans l'après midi pour se synchroniser.
