import math
import string 

passwordExists = False

while not passwordExists:
    #user input = password
    password = input("Enter Password: ")

    if not password:
        print("Password is empty.")
    else: 
        passwordExists = True
        

characterSets = {
    "lowercase": string.ascii_lowercase, 
    "uppercase": string.ascii_uppercase,
    "digits": string.digits,
    "punctuation": string.punctuation
}

poolSize = 0
#making sure the password provided by the user uses at least one charachter from each category
for characters in characterSets.values():
    if any(c in characters for c in password):
        poolSize += len(characters)

entropy = len(password) * math.log2(poolSize) if poolSize > 0 else 0 

strength = (
    "Extremely Weak" if entropy < 20 else
    "Very Weak" if entropy < 30 else
    "Weak" if entropy < 40 else
    "OK" if entropy < 60 else
    "Strong" if entropy < 80 else
    "Very Strong"
)

print(f"Entropy: {entropy:.1f} bits     |     Strength: {strength}")