#!/usr/bin/env python3

from string import ascii_lowercase as alphabet
from statistics import mode
from config import KEY


# Actual value is 0.065 but we approximate
INDEX_OF_COINCIDENCE_THRESHOLD = 0.06

# Because it comes in handy in several spots
alphabet_length = len(alphabet)

# When we start doing hacking and guess "the most common ciphertext
# char should be 'e'" for the ith character, we also check the
# 2nd, 3rd, 4th, ... C - 1, C chars. C stands for confidence
# we have in how well the passage represents expected English.
C = 5

# We will need to know the index of a letter in the alphabet frequently.
# Cut the computation time down with a hash table.
what_index_is = dict()
for i in range(alphabet_length):
    what_index_is[alphabet[i]] = i


def _shift(text, key=KEY, encrypt=True):
    """Takes text and shifts it according to the KEY.
    It can shift (encrypt) or reverse shift (decrypt)
    depending on if you set encrypt to {True, False}.
    :param text: the text you want to shift
    :param key: the key you want to use, default is KEY
    inside the config.py file
    :param encrypt: flag to encrypt or decrypt.
    Default is True.
    :type text: str
    :type key: str
    :type encrypt: bool
    """

    new_text = ''
    keylength = len(key)
    length = len(text)
    for i in range(length):

        # Find the index of the plaintext
        shift_value = what_index_is[text[i]]

        # Find the value of the key; if it overflows wrap around
        index = what_index_is[key[i % keylength]]

        # Based on what we're doing, we may decrypt or encrypt
        # So its index + shift_value + 1 % 26
        # The +1 is there because A is index 0 and wouldn't shift it,
        # but since we still want it mutating the plaintext, add 1
        if encrypt:
            new_text += alphabet[(index + shift_value + 1) % alphabet_length]
        else:
            new_text += alphabet[(shift_value - index - 1) % alphabet_length]
    return new_text


def _uglify(f):
    def wrapper(text):
        filtered = ''
        hash_table_alphabet = set(alphabet)
        for i in text:
            i = i.lower()
            filtered += i if i in hash_table_alphabet else ''
        return f(filtered.lower())
    return wrapper


@_uglify
def viginere_encrypt(text):
    n = len(KEY)
    blocks = [text[i:i+n] for i in range(0, len(text), n)]
    return ''.join(map(_shift, blocks))


@_uglify
def viginere_decrypt(ciphertext):
    n = len(KEY)
    blocks = [ciphertext[i:i+n] for i in range(0, len(ciphertext), n)]
    return ''.join(map(lambda x:_shift(x,encrypt=False), blocks))


@_uglify
def viginere_hack(ctext):
    def compute_ic(string):
        # Frequency vector
        f = [0] * alphabet_length

        # Count frequency of each letter occuring
        for i in string:
            f[what_index_is[i]] += 1

        # for each letter the index is
        #             f_i(f_i - 1)
        # C(f_i, 2) = ------------ (we can cancel the 2 though;
        #                  2        the denominator has one.)
        numerator = sum([(freq * (freq - 1)) for freq in f])
        n = len(string)
        try:
            return numerator / (n * (n - 1))
        except:
            return numerator

    got_key = False
    blocks = None
    #==========================================================================================
    # Step 1: Guess key length, i
    #==========================================================================================
    for i in range(1, len(ctext) + 1):
        print("Trying key length", i)
        
        # Break into k-sized blocks
        blocks = [ctext[j:j+i] for j in range(0, len(ctext), i)]
        
        # Consider the jth position of each block
        for j in range(i):
            # Concatenate the jth char for each string in blocks.
            # Compute the index of coincidence for those chars.
            chars_at_index_i = ''.join([string[j:j+1] for string in blocks])
            
            if compute_ic(chars_at_index_i) < INDEX_OF_COINCIDENCE_THRESHOLD:
                got_key = False
                break
            print("IC passed for char", i)
            got_key = True

        if got_key:
            print("Looks like keylength is", i)
            break
        elif i == len(ctext):
            print("=====================================================")
            print("Failed for all key attempts.")
            print("Is something wrong with the IC threshold?")
            print("Is this possibly not English?")
            print("=====================================================")
            return None

    #==========================================================================================
    # Step 2: we got the keylength, now take blocks and do analysis on them
    #==========================================================================================

    # These are the important variables from the last step
    keylength = i # Length of the key from the last iteration from Step 1
    blocks = blocks # This is the proper partition of the text
    n = len(blocks)
    
    # Most common letters in english are in the vector below
    most_likely = list('etaoinsrhldcumfpgwybvkxjqz')

    def determine_shift(cipherchar, guess):
        # We guess that "guess" ends at cipherchar after encryption.
        # Determine how much "guess" has to shift.
        # cipherchar = guess + shift =>
        # shift = cipherchar - guess.
        return what_index_is[cipherchar] - what_index_is[guess]

    key_matrix = [[]] * C
    for i in range(keylength):
        # Assume that one of the top 5 letters is 'e',
        # which asymptotically is true. Then use those
        # top 5 letters to see if any of them make a
        # word.

        ith_chars = [block[i:i+1] for block in blocks]
        f = [0] * alphabet_length
        for i in ith_chars:
            f[what_index_is[i]] += 1

        top_5_chars = f[0:C]
        for j in range(C):
            guess_shift = determine_shift(
                top_5_chars[i],
                most_likely[i]
            )
            key_matrix[j][i] += alphabet[guess_shift]

    #==========================================================================================
    # Step 3: We got a key matrix; now let's break the key.
    #==========================================================================================

    # Create our set() of english words
    english = set(open("english.txt").splitlines())

    # Something in here has to be in the hash table if everything worked correctly.
    key = ''
    not_found_key = True
    
    while not_found_key:
         
                



    return key
        

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="The viginere cipher")
    parser.add_argument("mode", choices=['e', 'd', 'h'], help="What action you want to take (h is for hack)")
    parser.add_argument("file", nargs='?', default='text.txt', type=str, help="The file you want to encrypt/decrypt")
    args = parser.parse_args()

    text = open(args.file).read()

    if args.mode == 'e':
        print(viginere_encrypt(text))
    elif args.mode == 'd':
        print(viginere_decrypt(text))
    else:
        print(viginere_hack(text))
