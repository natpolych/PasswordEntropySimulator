from entropy import ShannonEntropy, entropyCalc, strengthCategory
from bruteForce import bruteForceTime, timeConvert, multiSpeedBFA
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

        print(f"Password: {userPassword}")
        print(f"{'Theoretical Entropy:':<22}{round(theoretical,2):<10}bits  |  "f"{'Strength:':<10}{strengthCategory(theoretical)}")
        print(f"{'Shannon Entropy:':<22}{totalEntropy:<10}bits  |  "f"{'Strength:':<10}{strengthCategory(totalEntropy)}")

        times = multiSpeedBFA(userPassword)
        for attacker, t in times.items():
            print(f"{f'Brute-Force Time Against {attacker}:':<22}{t}")

        print("\n")

    print("Printing Graph Analysis")
    graphVisualizer(passwords)

if __name__ == "__main__":
    main()