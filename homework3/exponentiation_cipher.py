from string import ascii_lowercase as alphabet
from gmpy import invert

# KEY and PRIME must have gcd(KEY, PRIME - 1)=1
# so we can use FLT
KEY = 5
PRIME = 6599

# INVERSE denotes f. Normally you'd solve this with the reverse
# Euclidean algo, but I already implemented that so i use this
# to shave a few microseconds.
INVERSE = int(invert(KEY, PRIME - 1))

index = dict()
for i in range(len(alphabet)):
    index[alphabet[i]] = i

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
