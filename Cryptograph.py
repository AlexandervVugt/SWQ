from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

rsa_private_key_content = "-----BEGIN RSA PRIVATE KEY-----\
MIIBOAIBAAJAYNNFwOIra0R6GrKdRi2eFosX+bASK8ujCwUuWnxyO3Pp7FvTL/Yw\
/f4jSrT6RoA/ChMA93P487mAdJcjnS+UYQIDAQABAkA04AsuixQk7u8zVykV4uF6\
9BhyrRkvO3RdF0Y5+c2z8yj/467/YqNC1rS0pm3nNbHpYhRSaj6oOkytmMRnQunx\
AiEAvVAhrf0AavkpJN0GujBp8lmh7maBFlwurvKO5aPvqM0CIQCC7shXYIqzxnUw\
ecaGFqXeBigVxj3y1UfJuBH4X9fp5QIgH/Z8iTyzKlyBBtlOfncYHDPn9DFYUCcm\
NqF7YOhJ2W0CIH01/q7YqyvqwM0f14MJi4t8lb7k+v8LiYBVoBHHDkMlAiAyg2wm\
HtkwJ7C3qIgOKpkNAed3+YpeiGGshcIVP0JScQ==\
-----END RSA PRIVATE KEY-----"
rsa_public_key_content = "-----BEGIN PUBLIC KEY-----\
MFswDQYJKoZIhvcNAQEBBQADSgAwRwJAYNNFwOIra0R6GrKdRi2eFosX+bASK8uj\
CwUuWnxyO3Pp7FvTL/Yw/f4jSrT6RoA/ChMA93P487mAdJcjnS+UYQIDAQAB\
-----END PUBLIC KEY-----"

private_key = RSA.import_key(rsa_private_key_content)
public_key = RSA.import_key(rsa_public_key_content)

encryptor = PKCS1_OAEP.new(public_key, hashAlgo=SHA256)
decryptor = PKCS1_OAEP.new(private_key, hashAlgo=SHA256)