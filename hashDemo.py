import bcrypt
import hashlib

def SHA256Hash(password: str) -> str:
    """
    Returns the SHA-256 hash as a hexadecimal string
    """
    return hashlib.sha256(password.encode()).hexdigest()

def bcryptHash(password: str, rounds: int = 12) -> bytes:
    """
    Returns a salted(salt is generated automatically) bcrypt hash
    """
    salt = bcrypt.gensalt(rounds = rounds)
    return bcrypt.hashpw(password.encode(), salt)
