from entropy import entropyCalc, strengthCategory
from bruteForce import bruteForceTime
import matplotlib.pyplot as plt

strengthColours = {"Extremely Weak": "#ff4c4c", "Very Weak": "#ff944c", "Weak": "#ffcc4c", "OK": "#ffff4c", "Strong": "#4cff4c", "Very Strong": "#4cffb2"}

def graphVisualizer():
    """
    Passwords
    """
    if not passwords:
        print("Passwords don't exist")
        return

    """
    Calculations
    """
    theoretical = [entropyCalc(p) for p in passwords]
    shannon = [ShannonEntropy(p)[1] for p in passwords]
    strengths = [strengthCategory(e) for e in shannon]
    crackTime = [bruteForceTime(p, 1e9) for p in passwords]

    """
    1. Entropy comparison with Strength
    """
    x = range(len(passwords))
    width = 0.35
    
    plt.figure(figsize = (12,5))
    plt.bar([i - width/2 for i in x], theoretical, width = width, color = 'blue', label = "Theoretical Entropy") 
    plt.bar([i + width/2 for i in x], shannon, width = width, color = 'green', label= "Shannon Entropy")

    for i, s in enumerate(strengths):
        plt.text(i, max(theoretical[i], shannon[i]) + 0.5, s, ha = 'center', fontweight = 'bold', color = strengthColours.get(s, 'black'))

    plt.xticks(x, passwords)
    plt.ylabel("Entropy (bits)")
    plt.title("Password Entropy: Theoretical vs Shannon with Strength Category")
    plt.legend()
    plt.show()

    """
    2. Password Length vs Crack Time
    """
    lengths = [len(psw) for psw in passwords]

    plt.figure(figsize = (12,5))
    plt.bar(passwords, crackTimes, color = 'pink')
    plt.yscale("log") 
    plt.ylabel("Estimated Crack Time (seconds, log scale)")
    plt.title("Password Length vs Brute-Force Crack Time (1e9 guesses/sec)")
    plt.show()