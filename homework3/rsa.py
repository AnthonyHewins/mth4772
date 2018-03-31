from math import gcd
from euclidean_algorithm import extended_euclidean_algorithm as invert

#=========================================================
# Keys
#=========================================================
p = 137
q = 191
e = 79

#=========================================================
# Check keys, generate others
#=========================================================
n = (p-1) * (q-1)
if gcd(e, n) != 1:
    print("e must be relatively prime to phi(n)")
    exit()
else:
    global f
    # The second arg returned is the inverse of e, which is f by definition
    f = invert(e,n)[1] % n

def rsa_encrypt(plaintext):
    return pow(plaintext, e, n)

def rsa_decrypt(ctext):
    return pow(ctext, f, n)
