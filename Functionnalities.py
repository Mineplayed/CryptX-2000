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
    
def valid_shift(shift):
    not_valid = False
    
    if shift == "":
        os.system("cls")
        # Print this as an error
        print(colored("<============= ERREUR =============>", "red"))
        print(colored("Le décallage ne doit pas être vide", "red"))
        print(colored("Veuillez entrer un décallage valide", "red"))
        print(colored("<==================================>", "red"))
        
        print("\n")
        os.system("pause")
        not_valid = True
        return not_valid
    
    # Check if the shift is only digits
    for i in shift:
        if not i.isdigit():
            os.system("cls")
            
            print(colored("<================================ ERREUR ================================>", "red"))
            print(colored("Le décallage ne doit contenir que des chiffres", "red"))
            print(colored("Le décallage ne doit pas contenir de caractères spéciaux ni d'espaces", "red"))
            print(colored("Veuillez entrer un décallage valide", "red"))
            print(colored("<========================================================================>", "red"))
            
            print("\n")
            os.system("pause")
            not_valid = True
            return not_valid
        else:
            not_valid = False
            return not_valid

def type_choice():
    choice = str(input(colored("Voulez vous crypter ou décrypter votre message [C]/[D] ? ", "magenta")))    

    # If the user want to encrypt, it runs the function to encrypt
    if choice == "C" or choice == "c": 
        not_valid = "c"
        return not_valid
    # If the user want to decrypt, it runs the function to decrypt
    elif choice == "D" or choice == "d":
        not_valid = "d"
        return not_valid
    else:
        # If the user enter an invalid choice, it prints an error message
        os.system("cls")
        print(colored("<============= ERREUR =============>", "red"))
        print(colored("Votre choix doit être : [C] ou [D]", "red"))
        print(colored("Veuillez entrer un choix valide", "red"))
        print(colored("<==================================>", "red"))
        
        print("\n")
        os.system("pause")
        type_choice(choice)