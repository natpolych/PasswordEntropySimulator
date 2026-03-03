# PasswordEntropySimulator
A Python tool that calculates password entropy and simulates brute-force attacks

-entropy.py: 

    Description: Makes sure that the password isn't empty, figures out which character categories are being used (lowercase, uppercase, digits, punctuation), calcualtes theoretical password entropy ( (password length) * log_2(character pool size) ) and classifies password's strength.

    How does it work: The character pool depends on which character sets are used in the password (for example: if the password includes at least one uppercase letter then the pool size is 26, if it contains at least one digit then its 10 and if it contains both uppercase and digit, then the pool size iis 26 + 10 = 36 )
    Then we calculate the entropy, using: (password length) * log_2(character pool size). Higher entropy means higher resistance to brute-force attacks

    Note: entropy.py calculates the theoretical entropy, by making the assumptions that all characters are picked randomly and they all have the same probability of being used, it doesn't detect common passwords, or dictionary words or keyboard patterns
