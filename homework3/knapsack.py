from euclidean_algorithm import extended_euclidean_algorithm as invert
from math import gcd

#=======================================================================
# Key definition
#=======================================================================

# Your private keys
privkey = [2,9,15,28,52,105,250,502]
q = 1097
r = 149

# Your public key: multiply w through privkey mod q
pubkey = [(w * r) % q for w in privkey]

#=========================================================
# Check keys are valid
#=========================================================

# Check for valid sequence and prime
x = sum(privkey)
if q <= x:
    print((
        "Prime q cannot be less than the superincreasing sequence "
        "used as your key. q = %d, sequence sum = %d" % q, x
    ))
    exit()

# Check that the r is also valid
if gcd(r, q) != 1:
    print("gcd(r,q) must be one to use a knapsack cipher")
    exit()

#=========================================================
# Logic begins here
#=========================================================

def knapsack_encrypt(plainbits):
    """
    1. Multiply bit by each term in pubkey
    2. Sum it and return it as ciphertext
    """
    return sum([pubkey[i] * plainbits[i] for i in range(len(plainbits))])

def knapsack_decrypt(ctext):
    """
    1. Invert r and obtain the original sum
    2. Use greedy algo to determine the original bits
    """
    plaintext_sum = (invert(r, q)[1] * ctext) % q
    
    n = len(privkey)
    bitmap = [0] * n
    for i in range(n-1, -1, -1):
        if plaintext_sum >= privkey[i]:
            plaintext_sum -= privkey[i]
            bitmap[i] = 1

    return bitmap
