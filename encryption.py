import string

def encrypt(s,text):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
        if char not in string.ascii_letters:
            result += char
            continue
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

def main():
    text = input("Enter the text you want to encrypt: ")
    s = int(input("Enter the key you want to use: "))

    encrypted = encrypt(s,text)
    print(encrypted) 

if __name__ == "__main__":
    main()

