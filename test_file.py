from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization


def gen_key():
    private_key = ec.generate_private_key(
        ec.SECP256K1(), default_backend()
    )
    return private_key


key = gen_key()
public_key = key.public_key()

print(f"{public_key} is your extracted public key")