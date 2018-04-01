"""Elgamal

1. Pick a prime p and look at Z/pZ. Find a generator of Z/pZ.
2. Pick a random number a in [0,p-1] as your private key
3. Pick a random number k when you're about to send a message
   that can be changed each time you want to encode
4. Calculate two numbers:
      x = generator^k mod p
      y = ((generator^a)^k) * plaintext mod p
   This is the ciphertext
5. Given the two past numbers, calculate
      (x ^ (p - 1 - a)) * y mod p
"""
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
    return (pow(ctext1, p-1-a, p) * ctext2) % p
