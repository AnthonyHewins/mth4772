import random
from euclidean_algorithm import extended_euclidean_algorithm as invert
from string import ascii_lowercase as alphabet
from exponentiation_cipher import exp_encrypt, exp_decrypt
from knapsack import knapsack_encrypt, knapsack_decrypt
from rsa import rsa_encrypt, rsa_decrypt
from dh import find_generators
from eg import eg_encrypt, eg_decrypt

message = ""

# This runs for every problem to ensure the code worked.
def test(encrypt, decrypt, plaintext):
    print("=====================================================")
    print(message)
    
    print("Plaintext:", plaintext)
    ctext = encrypt(plaintext)
    print("Ciphertext:", ctext)
    decrypted_ciphertext = decrypt(ctext)
    print("Decrypted ciphertext:", decrypted_ciphertext)

    if plaintext == decrypted_ciphertext:
        print("Correct")
    else:
        print("Failed")

#=========================================================
# Problem 1: Exponentiation cipher.
#=========================================================
# Encrypt and decrypt the message 1000
# Message 1000 is equivalent to: str(alphabet[10]) + str(alphabet[00])
# I do something that's identical below, using division to speed it up.
message = "Problem 1: Exponential cipher"
plaintext = alphabet[1000 // 100]
plaintext += alphabet[1000 % 100]
test(exp_encrypt, exp_decrypt, plaintext)


#=========================================================
# Problem 2
#=========================================================
# Knapsack cipher, using the given superincreasing sequence.
message = "Problem 2: Knapsack cipher"
plaintext = [0,0,1,0,1,1,1,0]
test(knapsack_encrypt, knapsack_decrypt, plaintext)


#=========================================================
# Problem 3: RSA
#=========================================================
message = "Problem 3: RSA"
plaintext = 12345
test(rsa_encrypt, rsa_decrypt, plaintext)


#=========================================================
# Problem 4 (the code is so minimal I just do it right here)
#=========================================================
# Find all the generators of \mathbb{Z^*}_17.
# Then pick one for Diffie-Hellman.
generators = find_generators(17)
print("=====================================================")
print("Problem 4: Diffie-Hellman")
print("Generators:", generators)

# Public data for DH
random_generator = random.choice(list(generators))
p = 6599

# Secret data for DH
alices_a = random.randint(100,300)
bobs_b = random.randint(100,300)
print("Alice's key:", alices_a)
print("Bob's private key:", bobs_b)

# Information that bob and alice would receive from each other.
# bobs_g_to_the_a is what bob gets from Alice.
# alices_g_to_the_b is what alice gets from bob.
bobs_g_to_the_a = pow(random_generator,alices_a,p)
alices_g_to_the_b = pow(random_generator,bobs_b,p)
print("Alice's half-built key:", alices_g_to_the_b)
print("Bob's half-built key:", bobs_g_to_the_a)

# Then finish with another exponentiation
bobs_key = pow(bobs_g_to_the_a, bobs_b, p)
alices_key = pow(alices_g_to_the_b, alices_a, p)

print("Alice's fully built key:", alices_key)
print("Bob's fully built key:", bobs_key)
if bobs_key == alices_key:
    print("Correct")

#=========================================================
# Problem 5: Elgamal
#=========================================================
plaintext = 10
print("=====================================================")
print("Problem 5: Elgamal")
print("Plaintext:", plaintext)
ctext1, ctext2 = eg_encrypt(plaintext)
print("Ciphertexts:", ctext1, ctext2)
decrypted_ciphertext = eg_decrypt(ctext1, ctext2)
print("Decrypted ciphertext:", decrypted_ciphertext)
if decrypted_ciphertext == plaintext:
    print("Correct")
