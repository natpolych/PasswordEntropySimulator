from entropy import entropyCalc, strengthCategory, ShannonEntropy
from bruteForce import bruteForceTime, multiSpeedBFA
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

strengthColours = {"Extremely Weak": "#ff4c4c", "Very Weak": "#ff944c", "Weak": "#e6b800", "OK": "#ffcc4c", "Strong": "#4cff4c", "Very Strong": "#4cffb2"}

def graphVisualizer(passwords):
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

    for i in x:
        plt.plot(i+ width/2, shannon[i], marker = 'o', markersize = 8, color = 'black')
    for i, s in enumerate(strengths):
        plt.text(i, max(theoretical[i], shannon[i]) + 0.5, s, ha = 'center', fontweight = 'bold', color = strengthColours.get(s, 'black'))

    plt.xticks(x, passwords, rotation = 45)
    plt.ylabel("Entropy (bits)")
    plt.title("Password Entropy: Theoretical vs Shannon with Strength Category")

    strengthLegent = Line2D([0],[0], marker = 'o', color ='w', label='Strength (Based on Shannon Entropy)', markerfacecolor = 'black', markersize =8)
    
    plt.legend(handles = plt.gca().get_legend_handles_labels()[0] + [strengthLegent])
    plt.tight_layout()
    plt.show()

    """
    2. Password Length vs Crack Time
    """
    lengths = [len(p) for p in passwords]
    speeds =["Basic Attacker (1e6/sec)", "GPU Attacker (1e9/sec)", "Cluster Attacker (1e12/sec)"]
    colors = ["#ff9999", "#99ccff", "#99ff99"]

    timesDictionary = {speed: [] for speed in speeds }

    for p in passwords:
        times = multiSpeedBFA(p, return_seconds = True)
        for speed in speeds:
            timesDictionary[speed].append(times[speed])

    plt.figure(figsize = (12,6))
    width = 0.25
    for i, speed in enumerate(speeds):
        plt.bar([p + width * i - width for p in x], timesDictionary[speed], width = width, color = colors[i], label = speed)
    
    plt.xticks(x, passwords, rotation = 45)
    plt.yscale("log") 
    plt.ylabel("Estimated Crack Time (seconds, log scale)")
    plt.title("Password Length vs Brute-Force Crack Time (against all attacker types)")
    plt.legend()
    plt.tight_layout()
    plt.show()