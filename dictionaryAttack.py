import hashlib
from hashDemo import SHA256Hash

def dictionaryAttack(targetHash, wordlist = "wordlist.txt"):
    """
    Trying to crack a hash by using dictionary attack

    Parameters: targetHash (str) -> the hash we are trying to crack 
                wordlist (str) -> password list of common passwords

    Returns: if we crack the hash then it returns the cracked password, otherwise returns None
    """

    try:
        with open(wordlist, "r", encoding = "utf-8", errors = "ignore") as file:
            for word in file:
                password = word.strip()
                hashedWord = SHA256Hash(password)

                if hashedWord == targetHash:
                    return password

    except FileNotFoundError:
        print("Wordlist file not found.")

    return None