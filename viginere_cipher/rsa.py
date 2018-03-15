from keys import *


n = P * Q
phi_n = (P-1) * (Q-1)

def encrypt(message):
    pass


def decrypt(ctext):
    pass


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Does RSA encryption and decryption")
    parser.add_argument("mode", choices=['e', 'd'])
    parser.add_argument("message")
    args = parser.parse_args()

    
