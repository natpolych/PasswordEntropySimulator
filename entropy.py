import math
import string 

def entropyCalc(password):
    """
    Calculating theoretical maximum entropy of a password.
    Parameter: password (str)
    Returns: entropy (in bits)
    """
    
    characterSets = {                                                               #Dictionary that includes different categories of characters
        "lowercase": string.ascii_lowercase,                                        #abcdefghijklmnopqrstuvwxyz
        "uppercase": string.ascii_uppercase,                                        #ABCDEFGHIJKLMNOPQRSTUVWXYZ
        "digits": string.digits,                                                    #0123456789
        "punctuation": string.punctuation                                           #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    }

    poolSize = 0                                                                    #Amount of possible characters
    for characters in characterSets.values():                                       
        if any(c in characters for c in password):                                  #If the password contains at least one character from this category (lowercase, uppercase, digits, punctuation), then
            poolSize += len(characters)                                             #We add the whole category's size in the poolSize

    return len(password) * math.log2(poolSize) if poolSize > 0 else 0               #Calculating theoretical maximum entropy

def strengthCategory(entropy):
    """
    Classifying password's strength
    Parameter: entropy(float)
    Returns: strength category (str)
    """

    strength = (                                                                    #Password's strength based on the entropy
        "Extremely Weak" if entropy < 20 else
        "Very Weak" if entropy < 30 else
        "Weak" if entropy < 40 else
        "OK" if entropy < 60 else
        "Strong" if entropy < 80 else
        "Very Strong"
    )

    return strength