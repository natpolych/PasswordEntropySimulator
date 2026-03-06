# PasswordEntropySimulator
A Python tool that calculates password entropy and simulates brute-force attacks, hashing and dictionary attacks

Code Overview:
(src folder)
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


