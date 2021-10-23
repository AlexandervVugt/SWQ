def increment(salt):
    salt += 1
    return salt%128

def encrypt(content: str):
    salt = 1
    result = ""
    for char in content:
        result += chr(ord(char) + salt)
        salt = increment(salt)
    return result

def decrypt(content: str):
    salt = 1
    result = ""
    for char in content:
        result += chr(ord(char) - salt)
        salt = increment(salt)
    return result