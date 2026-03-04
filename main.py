from entropy import ShannonEntropy, entropyCalc, strengthCategory
from bruteForce import bruteForceTime
from visualizer import graphVisualizer

def main():

    passwords = []
    print("--------------------PASSWORD SECURITY SIMULATOR--------------------")
    print("Enter passwords (Write password and press Enter. To finish press Enter on empty input)")

    while True:
        userPassword = input(">>")
        if userPassword == "": break 
        passwords.append(userPassword)

    if not passwords:
        print("Password is empty")
        return

    print("\n-----------PASSWORD ANALYSIS-----------\n")
    for userPassword in passwords:
        theoretical = entropyCalc(userPassword)
        entropyPerCharacter, totalEntropy = ShannonEntropy(userPassword)
        crackTime = bruteForceTime(userPassword, 1e9)

        print(f"Password: {userPassword}")
        print(f"Theoretical Entropy: {round(theoretical, 2)} bits                                 |       Strength: {strengthCategory(theoretical)}")
        print(f"Shannon Entropy: {totalEntropy} bits (per character: {entropyPerCharacter})       |       Strength: {strengthCategory(totalEntropy)}")
        print(f"Estimated Brute-Force Time (1e9 guesses/sec): {timeConvert(crackTime)}")

    print("Printing Graph Analysis")
    graphVisualizer(passwords)

if __name__ == "__main__":
    main()