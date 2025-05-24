from termcolor import colored
import os

# Function to check if the message is not_valid
def valid_message(message):
    # Check if the message is empty
    if message == "":
        os.system("cls")
        # Print this as an error
        print(colored("<============= ERREUR =============>", "red"))
        print(colored("Le message ne doit pas être vide", "red"))
        print(colored("Veuillez entrer un message valide", "red"))
        print(colored("<==================================>", "red"))
        
        print("\n")
        os.system("pause")
        not_valid = True
        return not_valid
    
    # Check if the message is not_valid
    for i in message:
        if not i.isalpha() and not i.isdigit():
            os.system("cls")
            
            print(colored("<================================= ERREUR =================================>", "red"))
            print(colored("Le message ne doit contenir que des lettres et des chiffres", "red"))
            print(colored("Le message ne doit pas contenir de caractères spéciaux ni d'espaces", "red"))
            print(colored("Veuillez entrer un message valide", "red"))
            print(colored("<==========================================================================>", "red"))
            
            print("\n")
            os.system("pause")
            not_valid = True
            return not_valid
        
def valid_method_number(method_num):
    if method_num != "1" and method_num != "2" and method_num != "3" and method_num != "4" and method_num != "5":
        os.system("cls")
        # Print this as an error
        print(colored("<============= ERREUR =============>", "red"))
        print(colored("Votre choix doit être : [1], [2], [3], [4] ou [5]", "red"))
        print(colored("Veuillez entrer un choix valide", "red"))
        print(colored("<==================================>", "red"))
    
        print("\n")
        os.system("pause")
        not_valid = True
        return not_valid