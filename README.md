# PasswordEntropySimulator
A Python tool that calculates password entropy and simulates brute-force attacks, hashing and dictionary attacks

Code Overview:

src/

main.py

    Asks the user to enter passwords.
    For each password:
        •Calculates theoretical entropy (entropyCalc) and Shannon entropy (ShannonEntropy)
        •Determine strength category (strengthCategory) for both theoretical and Shannon entropy
        •Estimates brute-force attack times for different attacker speeds (multiSpeedBFA)
        •SHA-256 and bcrypt hashes
        •Dictionary attack, to see if we can recover a password that has been hashed (SHA-256 hash)
    Prints above results and calls visualizer (graphVisualizer), that generates 2 graphs.

entropy.py

    Measuring password entropy
        •entropyCalc(password) -> calculates the theoretical entropy, which is based on the password length and character sets(llwercase, uppercase, digits and puncuation) used.
        •ShannonEntropy(password) -> calculates Shannon entropy, which is based on frequency distribution of characters.
        •strengthCategory(entropy) -> returns a human readable strength label (Extremely Weak, Very Weak, Weak, OK, Strong, Very Strong)

bruteForce.py

        •bruteForceTime(password, guessesPerSec) -> estimates the time it would take (based on a given speed) to brute-force a password
        •multiSpeedBFA(password, return_seconds = False) -> estimates the time for multiple attacker speeds (Basic Attacker - 1e6 guesses/sec, GPU Attacker - 1e9 guesses/sec, Cluser Attacker - 1e12 guesses/sec)
    Returns time in a human readable form (or in seconds for the graph)

hashDemo.py

    Hashing passwords
        •SHA256Hash(password) -> returns SHA-256 hash as a hexadecimal string
        •bcryptHash(password, rounds = 12) -> returns bcrypt hash with salting
    Shows that bcrypt provides more security than SHA-256, even though it is slower.

dictionaryAttack.py

    Implements a dictionary attack against a password that has been hashed by SHA-256
    Reads passwords from data/worldlist.txt 
    Returns: the number of attempts and the time it took to crack the password (if cracked)
    If found returns cracked passwords, otherwise returns None

visualizer.py

    Generates two graphs
    -Graph 1: compares theoretical entropy vs Shannon entropy and has the strength categories (based on Shannon entropy) labeled above each password
    -Graph 2: Shows the estimated brute-force attack crack time for each attacker speed
    Saves graphs as pdf files in reports/

data/

wordlist.txt

    A list of commonly used passwords used for a dictionary attack

reports/

    1.Stores graph as pdf files
    2.Stores text reports with password analysis (example results for password I gave)
