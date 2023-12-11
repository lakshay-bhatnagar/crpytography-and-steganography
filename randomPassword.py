import hashlib
import random

def randomNumber():
    random_key = random.randint(1, 26)

    return random_key


def randomPassword(random_key):
    #random_key = random.randint(1, 2)

    
    key_str = str(random_key)

    hash_algorithm = hashlib.sha256()

    hash_algorithm.update(key_str.encode('utf-8'))

    hash_value = hash_algorithm.hexdigest()

    print("Random Number Key:", random_key)
    #print("Hashed Value (SHA-256):", hash_value)

    return hash_value

def main():
    x = randomNumber()
    randomPassword(x)

if __name__ == "__main__":
    main()
