import string
import random
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend




class Utils:

    

    def get_random_string(length):
        letters = string.ascii_uppercase
        proccesed_str = ''.join(random.choice(letters) for i in range(length))

        return proccesed_str

    def get_random_digits(length):
        digits = string.digits
        proccesed_digits = ''.join(random.choice(digits) for i in range(length))

        return proccesed_digits
    
    def generate_keys():
        key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=512
         )

        private_key = key.private_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PrivateFormat.PKCS8,
        crypto_serialization.NoEncryption()
        )

        public_key = key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
        )

        return {"public_key" : public_key, "private_key" : private_key}
        

