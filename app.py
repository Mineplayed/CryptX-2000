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
    print(result)

    #################
    # Caesar Cipher #
    #################

# Function to encrypt or decrypt message in Caesar Cipher
def Caesar(clear, result):
    # Ask for the offset of the encrypting
    offset = int(input("Indiquez le décalage : "))
    choice = str(input("Voulez vous crypter ou décrypter votre message [C]/[D] ? "))
    
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
    else:
        print("Your choice must be : [C] or [D]")
    print(result)

    ###################
    # Vigenere Cipher #
    ###################

# Function to generate the key and to make it as long as the message
def Vigenere_key(clear):
    key = str(input("Entrer votre clé de cryptage : "))
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
    print(encrypt_msg)
    # Return the result of all the calculs that led to the encrypt message
    return encrypt_msg

# Function to decrypt the Vigenere Cypher
# It takes the encrypted message, the repeated key and the string of the final result as parameters
def Decrypt_Vigenere(encrypted, key, decrypt_msg):
    
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
    print(decrypt_msg)

    ###################
    # Polybius Square #
    ###################
    
def Encrypt_polybius(clear):
    square_upper = ["ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZ0123", "456789"]
    square_lower = ["abcdef", "ghijkl", "mnopqr", "stuvwx", "yz0123", "456789"]
    charL_list = []
    sliced_squareL = []
    sliced_squareU = []
    character = []
    coord_char = []
    
    for i in clear:
        character.append(i)
    
    for char_list in square_lower:
        charL_list.append(char_list)

        squareL = []
        for i in range(6):
            squareL.append(char_list[i])
        sliced_squareL.append(squareL)
        
    for char_list in square_upper:
        squareU = []
        for i in range(6):
            squareU.append(char_list[i])
        sliced_squareU.append(squareU)

    for letter in character:
        line_count = 1  
        
        for line_char in sliced_squareL:
            column_char = []
            for i in range(len(line_char)):
                column_char.append(line_char[i])
                
                if column_char[i] == letter:
                    coord_char.append(line_count)
                    coord_char.append(len(column_char))
                
                if i > 4:
                    line_count += 1
        
        line_count = 1    
        for line_char in sliced_squareU:
            column_char = []
            for i in range(len(line_char)):
                column_char.append(line_char[i])
                
                if column_char[i] == letter:
                    coord_char.append(line_count)
                    coord_char.append(len(column_char))
                
                if i > 4:
                    line_count += 1
            
    print(coord_char)    

def Decrypt_polybius(encrypt):
    square = ["abcdef", "ghijkl", "mnopqr", "stuvwx", "yz0123", "456789"]
    line = []
    column = []
    chr_line = []
    decrypt = []
    
    for number in range(len(encrypt)):
        if number%2 == 0 or number == 0:
            line.append(int(encrypt[number]))
        else:
            column.append(int(encrypt[number]))
    
    count = 0
    for l in line:
        chr_line = square[l-1]
        for chr in range(len(chr_line)):
            if column[count] == chr + 1:
                decrypt.append(chr_line[chr])
        result = "".join(decrypt)
        count += 1
    print(result)
    
def Polybius(clear):
    choice = str(input("Voulez vous crypter ou décrypter votre message [C]/[D] ? "))
    
    if choice == "C":
        Encrypt_polybius(clear)
    elif choice == "D":
        Decrypt_polybius(clear)
        
def App():
    print("Vous pouvez choisir n'importe quelles méthodes de cryptages entre: ")
    print("Le ROT13 -> [1]")
    print("Le code César -> [2]")
    print("Le chiffre de Vigenère -> [3]")
    print("Le carré de Polybe -> [4]")
    choice = str(input("Quel est votre choix: [1], [2], [3] ou [4] ? "))
    clear_message = input("Indiquez votre message à crypter : ")
    
    result = ""
    
    match choice:
        case "1":
            ROT13(clear_message, result)
        case "2":
            Caesar(clear_message, result)
        case "3":
            key = Vigenere_key(clear_message)
            encrypt_msg = Encrypt_vigenere(clear_message, key, result) 
            Decrypt_Vigenere(encrypt_msg, key, result)
        case "4":
            Polybius(clear_message)

App()

# Rajouter colorama pour les couleurs