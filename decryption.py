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
    encrypted = input("Enter the encrypted text you want to decrypt: ")
    s = int(input("Enter the key you want to use: "))

    decrypted = decrypt(s,encrypted)
    print(decrypted) 

if __name__ == "__main__":
   main()
