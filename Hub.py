import os

os.system("cls")

# Print the hub menu
print("<======================= HUB =======================>")
print("\n")
print("Bienvenue dans le Hub de l'application !")
print("\n")
print("Ce Hub vous permet de lancer l'application CryptX-2000 et de gérer les dépendances nécessaires.")
print("\n")
print("Vous pouvez choisir une fonctionnalité parmi celles proposées :")
print("1. Installer les dépendances")
print("2. Lancer l'application")
print("3. Quitter l'application")

print("\n")

def valid_choice():
    choice = input("Veuillez entrer votre choix : ")
    
    if choice != "1" and choice != "2" and choice != "3":
        os.system("cls")
        # Print this as an error
        print("<======================= ERREUR =======================>")
        print("Votre choix doit être : [1], [2] ou [3]")
        print("Veuillez entrer un choix valide")
        print("<======================================================>")
        
        print("\n")
        os.system("pause")
        valid_choice()
    else:
        match choice:
            case "1":
                os.system("cls")
                print("<======================= INSTALLATION =======================>")
                
                print("\n")
                print("Installation des dépendances en cours...")
                os.system("Installation.bat")
                print("\n")
                print("Vous pouvez maintenant lancer l'application.")
                print("\n")
                
                print("<============================================================>")
                
                print("\n")
                os.system("pause")
            case "2":
                os.system("cls")
                print("<======================= LANCEMENT =======================>")
                
                print("\n")
                print("Lancement de l'application...")
                os.system("CryptX-2000_app.bat")
            case "3":
                os.system("cls")
                print("<======================= AU REVOIR =======================>")
                
                print("\n")
                print("Merci d'avoir utilisé l'application !")
                print("\n")
                
                print("<=========================================================>")
                
                print("\n")
                os.system("pause")
                exit()

valid_choice()