import applicationBackend


class Application:

    def __init__(self, nom="", version="", auteur="", licence=""):
        self.nom = nom
        self.version = version
        self.auteur = auteur
        self.licence = licence

    @staticmethod
    def getAllapplicationFromNexus():
        lst = []
        lst_app = applicationBackend.getComponents()
        for app in lst_app:
            app = Application(app["name"], app["version"], "Gelasse Kevin", None)
            lst.append(app)
        for i in lst:
            print("Auteur: " + str(i.auteur) + " Licence: " + str(i.licence) + " Nom de l'application: " + str(i.nom) + " Version: " + str(i.version))

