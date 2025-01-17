from termcolor import colored
from pyfiglet import Figlet
import os

    ################
    # ROT13 Cipher #
    ################

# Function to encrypt or decrypt message in ROT13
def ROT13(clear, result):    
    # Loop for each letters
    for i in range(len(clear)):
        letter = clear[i]  
        # Encrypt or decrypt lower letters
        if (letter.islower()):
            result += chr((ord(letter) - 84) % 26 + 97)
        # Encrypt or decrypt upper letters
        else:
            result += chr((ord(letter) - 52) % 26 + 65)
    print(colored("Le résultat du cryptage est:", "blue"))
    print(colored(result, "light_blue"))

    #################
    # Caesar Cipher #
    #################

# Function to encrypt or decrypt message in Caesar Cipher
def Caesar(clear, result):
    # Ask for the offset of the encrypting
    offset = int(input(colored("Indiquez le décalage: ", "light_green")))
    choice = str(input(colored("Voulez vous crypter ou décrypter votre message [C]/[D] ? ", "magenta")))
    
    if choice == "C":
        # Loop for each letters in the message 
        for i in range(len(clear)):
            letter = clear[i]
            # Encrypt or decrypt lower letters
            if (letter.islower()):
                result += chr((ord(letter) + offset - 97) % 26 + 97)
            # Encrypt or decrypt upper letters
            else:
                result += chr((ord(letter) + offset - 65) % 26 + 65)
        print(colored("Le résultat du cryptage est:", "blue"))
        print(colored(result, "blue"))
    elif choice == "D":
        # Loop for each letters in the message 
        for i in range(len(clear)):
            letter = clear[i]
            # Encrypt or decrypt lower letters
            if (letter.islower()):
                result += chr((ord(letter) - offset - 97) % 26 + 97)
            # Encrypt or decrypt upper letters
            else:
                result += chr((ord(letter) - offset - 65) % 26 + 65)
        print(colored("Le résultat du décryptage est:", "blue"))
        print(colored(result, "light_blue"))
    else:
        print(colored("Your choice must be : [C] or [D]", "red"))

    ###################
    # Vigenere Cipher #
    ###################

# Function to generate the key and to make it as long as the message
def Vigenere_key(clear):
    key = str(input(colored("Entrer votre clé de cryptage : ", "yellow")))
    repeated_key = []
    count = 0
    
    # Loop for each letters in the message
    for i in range(len(clear)):
        # Create a list with the repettion of the key.
        # Look when it put all letters one time in this list, it goes back to the fisrt character 
        # and write another time the key in the list 'till the list is exactly as long as the message
        if count < len(key):
            repeated_key.append(key[count])
            # Manual increment for the key character counter
            count += 1
        else:
            # Put the key character counter down to 0 when it reaches the end of the key
            count = 0
            repeated_key.append(key[count])
            count += 1
    # Return the list with the repetition of the key, which is now as long as the message
    return repeated_key

# Function to encrypt message in Vigenere Cipher
def Encrypt_vigenere(clear, key, encrypt_msg):
    # Loop for each character in the message
    for i in range(len(clear)):
        # Look if it's letter in the alphabet or not
        # If it is, it search the shift between the message en the key 
        if clear[i].isalpha():
            # Search the shift
            shift = ord(key[i].upper()) - ord("A")
            # If the letter is a lowercase, it add to the string "encrypt_msg" the character linked
            # to the Unicode of the number i character in the message plus the shift minus the Unicode
            # of the first lowercase letter, "a", then it find the rest of the division by 26 
            # to finally add the Unicode of the lowercase letter "a".
            if clear[i].islower():
                encrypt_msg += chr((ord(clear[i]) + shift - ord("a")) % 26 + ord("a"))
            # The same as the previous line but with upper letters
            else:
                encrypt_msg += chr((ord(clear[i]) + shift - ord("A")) % 26 + ord("A"))
        # If it's not a letter from the alphabet, it add to the string "encrypt_msg" the unchanged character from the message
        else:
            encrypt_msg += clear[i]
    print(colored("Le résultat du cryptage est:", "blue"))
    print(colored(encrypt_msg, "light_blue"))

# Function to decrypt the Vigenere Cypher
# It takes the encrypted message, the repeated key and the string of the final result as parameters
def Decrypt_vigenere(encrypted, key, decrypt_msg):
    
    for i in range(len(encrypted)):
        # Look if it's letter in the alphabet or not
        # If it is, it search the shift between the message en the key 
        if encrypted[i].isalpha():
            # Search the shift
            shift = ord(key[i].upper()) - ord("A")
            # If the letter is a lowercase, it add to the string "decrypt_msg" the character linked
            # to the Unicode of the number i character in the message minus the shift added by the first shift,
            # needed to encrypt the message, minus the Unicode of the first lowercase letter, "a", 
            # then it find the rest of the division by 26 to finally add the Unicode of the lowercase letter "a".
            if encrypted[i].islower():
                decrypt_msg += chr((ord(encrypted[i]) - shift - ord("a")) % 26 + ord("a"))
            # The same as the previous line but with upper letters
            else:
                decrypt_msg += chr((ord(encrypted[i]) - shift - ord("A")) % 26 + ord("A"))
        # If it's not a letter from the alphabet, it add to the string "decrypt_msg" the unchanged character from the message
        else:
            decrypt_msg += encrypted[i]
    print(colored("Le résultat du décryptage est:", "blue"))
    print(colored(decrypt_msg, "light_blue"))

    ###################
    # Polybius Square #
    ###################
    
# Function that encrypt with the vigenere cipher 
def Encrypt_polybius(clear):
    # Creation of the square i'll be using:
    # 0, 1,2,3,4,5,6
    # 1, a,b,c,d,e,f
    # 2, g,h,i,j,k,l
    # 3, m,n,o,p,q,r
    # 4, s,t,u,v,w,x
    # 5, y,z,0,1,2,3
    # 6, 4,5,6,7,8,9
    # For the uppercase letters then the lowercase letters
    # Creation of all other variables
    upper_square = ["ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZ0123", "456789"]
    lower_square = ["abcdef", "ghijkl", "mnopqr", "stuvwx", "yz0123", "456789"]
    characters = []
    coord_char = []
    
    # For each letter in the message, it adds it in the list characters
    for i in clear:
        characters.append(i)
        
    # For each letter in the list characters, it resets the line counter to 1
    for letter in characters:
        
        #  For each line, it resets the variable column_char
        line_count = 1  
        for line_char in lower_square:
            column_char = []
            # Adds every lines to the variable column_char and look each time 
            # if the letter we're looking for is in the line,then,if it is, 
            # it adds to the variable coord_char the line number then the column number of the letter in this line
            for i in range(len(line_char)):
                column_char.append(line_char[i])
                
                if column_char[i] == letter:
                    coord_char.append(line_count)
                    coord_char.append(len(column_char))
                
                # When i is on the last character it adds 1 to the line and it change the line
                if i > 4:
                    line_count += 1

        #  For each line, it resets the variable column_char and then do the same algorythm as the one just before but with uppercase letters
        line_count = 1    
        for line_char in upper_square:
            column_char = []
            for i in range(len(line_char)):
                column_char.append(line_char[i])
                
                if column_char[i] == letter:
                    coord_char.append(line_count)
                    coord_char.append(len(column_char))
                
                if i > 4:
                    line_count += 1
        
    # Print the result of the encrypt
    print(colored("Le résultat du cryptage est:", "green"))
    print(colored(coord_char, "light_green"))

# Function to decrypt the polybius cipher
def Decrypt_polybius(encrypt):
    # Creation of the square i'll be using:
    # 0, 1,2,3,4,5,6
    # 1, a,b,c,d,e,f
    # 2, g,h,i,j,k,l
    # 3, m,n,o,p,q,r
    # 4, s,t,u,v,w,x
    # 5, y,z,0,1,2,3
    # 6, 4,5,6,7,8,9
    # Creation of all other variables
    square = ["abcdef", "ghijkl", "mnopqr", "stuvwx", "yz0123", "456789"]
    line = []
    column = []
    chr_line = []
    decrypt = []
    
    # For each number of the encrypted message, look if it have an index which is pair, it adds its value to the variable line
    for number in range(len(encrypt)):
        if number%2 == 0 or number == 0:
            line.append(int(encrypt[number]))
        # If its an index which is impair, it adds it to the column variable
        else:
            column.append(int(encrypt[number]))
    
    # For each line in the list of lines, it assign to the variable chr_line the square coresponding line 
    count = 0
    for l in line:
        chr_line = square[l-1]
        # For each character in the range of the line, it look if the column index correspond to the right character, otherwise it look on the next column
        # Then it adds to the variable decrypt, the character coresponding the column in the line
        for chr in range(len(chr_line)):
            if column[count] == chr + 1:
                decrypt.append(chr_line[chr])
        # It erease all double quotes from the list
        result = "".join(decrypt)
        count += 1
    
    # It print the result of the decrypt 
    print(colored("Le résultat du décryptage est:", "green"))
    print(colored(result, "light_green"))
    
    #######
    # App #
    #######

def Vigenere(clear, result):
    choice = str(input(colored("Voulez vous crypter ou décrypter votre message [C]/[D] ? ", "magenta")))
    
    if choice == "C":
        key = Vigenere_key(clear)
        Encrypt_vigenere(clear, key, result) 
    elif choice == "D":
        key = Vigenere_key(clear)
        Decrypt_vigenere(clear, key, result)
    
def Polybius(clear):
    choice = str(input(colored("Voulez vous crypter ou décrypter votre message [C]/[D] ? ", "magenta")))
    
    if choice == "C":
        Encrypt_polybius(clear)
    elif choice == "D":
        Decrypt_polybius(clear)
        
def Presentation():
    f = Figlet(font="standard")
    print(colored(f.renderText("CryptX 2000"), "magenta"))
    
    
    print(colored("Vous pouvez choisir n'importe quelles méthodes de cryptages entre: ", "blue"))
    print(colored("Le ROT13 -> [1]", "light_blue"))
    print(colored("Le code César -> [2]", "light_blue"))
    print(colored("Le chiffre de Vigenère -> [3]", "light_blue"))
    print(colored("Le carré de Polybe -> [4]", "light_blue"))
    choice = str(input(colored("Quel est votre choix: [1], [2], [3] ou [4] ? ", "light_red")))
    clear_message = input(colored("Indiquez votre message à crypter : ", "cyan"))
    
    return choice, clear_message
        
def App():
    os.system("cls")
    
    result = ""
    f = Figlet(font="bulbhead")
    
    choice, clear = Presentation()
    os.system("cls")
    
    match choice:
        case "1":
            print(colored(f.renderText("ROT 13"), "magenta"))
            ROT13(clear, result)
        case "2":
            print(colored(f.renderText("Ceasar"), "magenta"))
            Caesar(clear, result)
        case "3":
            print(colored(f.renderText("Vigenère"), "magenta"))
            Vigenere(clear, result)
        case "4":
            print(colored(f.renderText("Polybe"), "magenta"))
            Polybius(clear)
            
App()

# Rajouter termcolor pour les couleurs
# Faire attention a etre en version 3.12
# Install pip

# Rajouter un ascii art au début pour présenter

# Au début il faut installer python 3.12, puis termcolor, puis pygfiglet a l'aide de pip