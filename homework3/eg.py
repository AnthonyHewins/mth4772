from dh import find_generators
from random import randint

#==============================================================================
# Key definition
#==============================================================================
# Public key tuple: our prime, generator, and random private key
# (Alice's private key)
p = 17
r = 3
a = randint(0,p-1)

#==============================================================================
# Code
#==============================================================================
def eg_encrypt(plaintext):
    k = randint(1, p-2)
    b = pow(r, a, p)
    return pow(r, k, p), ((b ** k) * plaintext) % p

def eg_decrypt(ctext1, ctext2):
    return (pow(ctext1, p-1-a % p, p) * ctext2) % p
