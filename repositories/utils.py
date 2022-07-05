import string
import random
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization





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
        key = ec.generate_private_key(
        ec.SECP256K1(), default_backend())


        private_key = format(key.private_numbers().private_value, '064x')
        

        return {"message" : "your private is generated",  "private_key" : private_key}
        

