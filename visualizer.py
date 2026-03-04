from entropy import entropyCalc, strengthCategory
from bruteForce import bruteForceTime
import matplotlib.pyplot as plt

def graphVisualizer():
    """
    User input
    """
    passwords = []
    print("Enter passwords (Write password and press Enter. To finish press Enter on empty input)")

    while True:
        userPassword = input(">>")
        if userPassword == "": break 
        passwords.append(userPassword)

    if not passwords:
        print("Passwords don't exist")
        exit()

    """
    Calculations
    """
    entropies = [entropyCalc(p) for p in passwords]
    strengths = [strengthCategory(e) for e in entropies]
    crackTime = [bruteForceTime(p, 1e9) for p in passwords]

    """
    1. Entropy vs Strength
    """
    strengthMap = {
        "Extremely Weak": 1, 
        "Very Weak": 2, 
        "Weak": 3, 
        "OK": 4, 
        "Strong": 5, 
        "Very Strong": 6
    }

    strengthVals = [strengthMap[s] for s in strengths]

    plt.figure(figsize = (10,5))
    plt.bar(passwords, entropies, color = 'blue')

    for i, s in enumerate(strengths):
        plt.text(i, entropies[i] + 0.5, s, ha = 'center', fontweight = 'bold')

    plt.ylabel("Entropy (bits)")
    plt.title("Password Entropy vs Strength")
    plt.show()

    """
    2. Password Length vs Crack Time
    """
    crackTimes  = [bruteForceTime(psw, 1e9) for psw in passwords]
    lengths = [len(psw) for psw in passwords]

    plt.figure(figsize = (10,5))
    plt.bar(passwords, crackTimes)

    plt.yscale("log") 

    plt.ylabel("Estimated Crack Time (seconds, log scale)")
    plt.title("Password Length vs Brute-Force Crack Time (1e9 guesses/sec)")

    plt.show()