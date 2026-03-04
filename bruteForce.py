from entropy import entropyCalc

def bruteForceTime(password, guessPerSec = 1e9):
    """
    Here we are going to estimate the time it takes to crack a password by brute-force attack, using entropy
    combinations = 2 ^ entropy
    """
    entropy = entropyCalc(password)
    combinations = 2 ** entropy
    seconds = combinations / guessPerSec

    return seconds

def timeConvert(seconds):
    """
    Converting seconds into minutes / hours / days / years
    """

    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    if years >= 1: return f"{years:.2f} years"
    elif days >= 1: return f"{days:.2f} days"
    elif hours >= 1: return f"{hours:.2f} hours"
    elif minutes >= 1: return f"{minutes:.2f} minutes"
    else: return f"{seconds:.2f} seconds"

def multiSpeedBFA(password, return_seconds = False):
    """
    Calculating crack time for different attacker speeds
    returns: human-readable time
    """

    speeds = {"Basic Attacker (1e6/sec)": 1e6, "GPU Attacker (1e9/sec)": 1e9, "Cluster Attacker (1e12/sec)": 1e12}
    results = {}

    for label, speed in speeds.items():
        seconds = bruteForceTime(password, speed)
        results[label] = seconds if return_seconds else timeConvert(seconds)

    return results