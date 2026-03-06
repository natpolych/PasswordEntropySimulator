from entropy import ShannonEntropy, entropyCalc, strengthCategory
from bruteForce import bruteForceTime, timeConvert, multiSpeedBFA
from visualizer import graphVisualizer
from hashDemo import SHA256Hash, bcryptHash
from dictionaryAttack import dictionaryAttack

def main():

    passwords = []
    print("="*100)
    print("|"," "*35,"PASSWORD SECURITY SIMULATOR"," "*32, "|")
    print("="*100)
    print("Enter passwords (Write password and press Enter. To finish press Enter on empty input)")

    while True:
        userPassword = input(">>")
        if userPassword == "": break 
        passwords.append(userPassword)

    if not passwords:
        print("Password is empty")
        return
    print("="*100)
    print("|"," "*40,"PASSWORD ANALYSIS"," "*37, "|")
    print("="*100)
    for userPassword in passwords:

        print(f"Password: {userPassword}")
        print("-"*50)

        theoretical = entropyCalc(userPassword)
        tStrength = strengthCategory(theoretical)
        shannon = ShannonEntropy(userPassword)[1]
        sStrength = strengthCategory(shannon)
        print(f"->Entropy Analysis")
        print(f"{'Theoretical Entropy:':<25}{theoretical:>5.2f} bits | {'Strength:':<10} {tStrength}")
        print(f"{'Shannon Entropy:':<25}{shannon:>5.2f} bits | {'Strength:':<10} {sStrength}\n")
        print(f"->Brute Force Estimation")

        times = multiSpeedBFA(userPassword)
        maxLabelLength = max(len(f"Brute-Force Time Against {attacker}:") for attacker in times)
        for attacker, t in times.items():
            label = f"Brute-Force Time Against {attacker}:"
            print(f"{label:<{maxLabelLength}}   {t}")

        print("\n->Hashing")
        sha = SHA256Hash(userPassword)
        print(f"SHA-256:    {sha}")
        bcr = bcryptHash(userPassword).decode()
        print(f"bcrypt:     {bcr}\n")

        print(f"->Dictionary Attack (for SHA-256)")
        cracked = dictionaryAttack(sha)

        pswFound, attempts, elapsed = dictionaryAttack(sha)
        if pswFound:
            print("Password Found!")
            print(f"Recovered Password:         {pswFound}")
            print(f"Attempts:                   {attempts}")
            print(f"Time:                       {elapsed:.4f} seconds")
        else:
            print("Password not found")
            print(f"Attempts:                   {attempts}")
            print(f"Time:                       {elapsed:.4f} seconds")

        print("\n")
        print("-"*50)

    print("Printing Graph Analysis")
    #graphVisualizer(passwords)

if __name__ == "__main__":
    main()