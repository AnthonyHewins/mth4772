"""The exponential cipher
Definitions:
    "===" := congruent to

Based on the fact that 1. an inverse exists for any number k
relatively prime to a prime p and 2. no information loss occurs
to the original number if the prime is sufficiently large.

Plaintext^k === N mod p
N ^ inverse(k) === Plaintext mod p

1. Take your text and encode it. Split it into 2-tuples:
   AA -> 00, AB -> 01, BB -> 11, ...
2. For each block, raise it to the KEY power and mod it to
   PRIME. Send this.
3. Receive 2. Raise it to the INVERSE power
   (How can we guarantee that KEY has an inverse?
   Require that gcd(KEY, PRIME) = 1). Now decode.
"""

from math import gcd
from string import ascii_lowercase as alphabet
from gmpy import invert

#==============================================================================
# Key Definition
#==============================================================================
KEY = 5
PRIME = 6599

if gcd(KEY, PRIME) != 1:
    print("Must have gcd of 1 between KEY and PRIME otherwise can't use FLT")

INVERSE = int(invert(KEY, PRIME - 1))

# All this does is look up the index of a letter in the alphabet
index = dict()
for i in range(len(alphabet)):
    index[alphabet[i]] = i

#==============================================================================
# Code
#==============================================================================
def exp_encrypt(text):
    # Chop into pieces that are 2 chars long
    blocks = [text[i:i+2] for i in range(0,len(text),2)]
    
    # Concatenate two ints together like so:
    # Given 'cd' in the above,
    # C -> alphabet[2] means its code is 02
    # D -> alphabet[3] means its code is 03
    # We should see 0203.
    int_blocks = []
    for i in blocks:
        if len(i) != 1:
            int_blocks += [(index[i[0]] * 100) + index[i[1]]]
        else:
            int_blocks += [index[i[0]] * 100]

    # The encryption process
    return [pow(i, KEY, PRIME) for i in int_blocks]

def exp_decrypt(ctext):
    # Decrypt with our key
    decrypted_blocks = [pow(i, INVERSE, PRIME) for i in ctext]

    # Rebuild the word
    plaintext = ''
    for i in range(len(decrypted_blocks)):
        block = decrypted_blocks[i]
        plaintext += alphabet[block // 100]
        plaintext += alphabet[block % 100]

    return plaintext
