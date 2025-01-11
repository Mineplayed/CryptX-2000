clear_message = input("Indiquez votre message à crypter : ")
result = ""

# Function to encrypte or decrypt message in ROT13
def ROT13(clear):    
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
# ROT13(clear_message)

# Function to encrypt or decrypt message in Caesar Cipher
def Caesar(clear):
    # Ask for the offset of the encrypting
    offset = int(input("Indiquez le décalage : "))
    
    # Loop for each letters 
    for i in range(len(clear)):
        letter = clear[i]
        # Encrypt or decrypt lower letters
        if (letter.islower()):
            result += chr((ord(letter) + offset - 97) % 26 + 97)
        # Encrypt or decrypt upper letters
        else:
            result += chr((ord(letter) + offset - 65) % 26 + 65)
    print(result)
# Caesar(clear_message)

# Function to encrypt or decrypt message in Vigenere Cipher
def Vigenere(clear):
    sliced_clear = []
    sliced_key = []
    repeated_key = []
    key = str(input("Entrer votre clé de cryptage : "))
    
    # Separate all letters of the key
    count = 0
    for i in key:
        sliced_key.append(key[count])
        count += 1
        
    count = 0
    for i in clear:
        sliced_clear.append(clear[count])
        count += 1
    print(sliced_key, sliced_clear)
    
    count = 0
    for i in sliced_clear:
        if count < len(sliced_key):
            repeated_key.append(sliced_key[count])  
        else:
            count = 0
            repeated_key.append(sliced_key[count])
        count += 1
        
    repeated_number_clear = []
    count = 0
    for i in repeated_key:
        char = sliced_clear[count]
        count += 1
        if (char.islower()):
            repeated_number_clear.append(str((ord(char) - 97) % 26 + 97))
        else:
            repeated_number_clear.append(str((ord(char) - 65) % 26 + 65))
    print(repeated_number_clear)

Vigenere(clear_message)