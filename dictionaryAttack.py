import hashlib
from hashDemo import SHA256Hash
import time

def dictionaryAttack(targetHash, wordlist = "wordlist.txt"):
    """
    Trying to crack a hash by using dictionary attack

    Parameters: targetHash (str) -> the hash we are trying to crack 
                wordlist (str) -> password list of common passwords

    Returns: if password is found then it returns the password, the attempts and the time elapsed
    """
    attempts = 0
    startT = time.time()
    try:
        with open(wordlist, "r", encoding = "utf-8", errors = "ignore") as file:
            for word in file:
                password = word.strip()
                attempts += 1
                hashedWord = SHA256Hash(password)

                if hashedWord == targetHash:
                    elapsed = time.time() - startT
                    return password, attempts, elapsed

    except FileNotFoundError:
        print("Wordlist file not found.")
        return None, attempts, 0

    elapsed = time.time() - startT
    return None, attempts, elapsed