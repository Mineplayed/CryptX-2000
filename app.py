list = input("Indiquez votre message à crypter : ")

# reprendre avec le tableau asscii utf-8

def ROT13(list):
    rot13 = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
    print(list.translate(rot13))
    
ROT13(list)

def encrypt(list):
    offset = int(input("Indiquez le décalage : "))
    result = ""

    # traverse text
    for i in range(len(list)):
        char = list[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + offset - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + offset - 97) % 26 + 97)
            
    print(result)

encrypt(list)