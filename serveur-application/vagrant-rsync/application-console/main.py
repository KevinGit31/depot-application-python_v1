import crud


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    while True:
        isNumber = True
        print_hi('****Bienvenue sur notre application****')
        print_hi("Que souhaitez-vous faire aujourd'hui ?")
        print_hi("1 - Lister toutes les machines du parc.")
        print_hi("2 - Chercher une machine en particulier sur le parc.")
        print_hi("3 - Ajouter une nouvelle machine au parc.")
        print_hi("4 - Supprimer une machine du parc.")
        print_hi("5 - Mise à jour d'une machine du parc.")
        print_hi("6 - Lister les versions d'applications disponibles sur le serveur de Nexus.")
        print_hi("7 - Sortir de l'application.")
        while isNumber:
            choice_user = input("Choisissez entre les différentes options: ")
            try:
                choice_user = int(choice_user)
                isNumber = False
            except:
                print("La valeur saisie n'est pas un nombre")
        if choice_user == 1:
            print("Liste des machines du parc:")
            print(str(crud.get_machines()))
        elif choice_user == 2:
            hostname = input("Veuillez saisir le hostname de la machine pour avoir les informations: ")
            data = crud.get_machine(hostname)
            print(str(data))
        elif choice_user == 3:
            print("Bienvenue sur l'interface d'ajout d'une nouvelle machine")
            crud.create_machine()
            print("Votre nouvelle machine a été créée!")
        elif choice_user == 4:
            hostname = input("Veuillez saisir le hostname d'une machine à supprimer: ")
            data = crud.delete_machine(hostname)
            print(str(data))
        elif choice_user == 5:
            print("Bienvenue sur l'interface de mise à jour d'une machine")
            hostname = input("Veuillez saisir le hostname de la machine à modifier: ")
            data = crud.update_machine(hostname)
            print(str(data))
        elif choice_user == 6:
            print("applinexus")
        elif choice_user == 7:
            print("Aurevoir !")
            break
        else:
            print("Action répertorié, aurevoir!")
            break

