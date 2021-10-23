def increment(salt):
    salt += 1
    return salt%128

def cypher(content: str, encrypt: bool):
    salt = 1
    result = ""
    for char in content:
        if encrypt:
            result += chr(ord(char) + salt)
        else:
            result += chr(ord(char) - salt)
        salt = increment(salt)
    return result