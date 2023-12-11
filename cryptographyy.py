import string
import steganograpy as stg
import randomPassword as rndpwd


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

def decrypt(s,message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - s) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result
   

def main():

    s = rndpwd.randomNumber()
    while(1):
        print("What do you want to do : \n(1) Encrytion in Caeser Cipher \n(2) Decryption in Caeser Cipher \n(3) Exit")
        choice=int(input())
        if choice==1:
            text = input("Enter the text you want to encrypt: ")
            hashed_key = rndpwd.randomPassword(s)
            print(hashed_key)
            img_path = input("Enter the path to the image: ")

            encrypted = encrypt(s,text)
            stg.encode_image(img_path,encrypted)
            print(encrypted)
            print("Encrypted message encoded successfully")
            print("\n")

        if choice==2:
            print("What do you want to do: \n(1)Decrypt a message\n(2)Decode the text in image")
            option=int(input())
            if option==1:
                message = input("Enter the encrypted message: ")
                #s = int(input("Enter the key used for encryption: "))
                decrypted = decrypt(s,message)
                print(decrypted)
            if option==2:
                encoded_img_path = input("Enter the path to the encoded image: ")
                stg.decode(encoded_img_path)
            print("\n")
        if choice==3:
            break
     

if __name__ == "__main__":
   main()