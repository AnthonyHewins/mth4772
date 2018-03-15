import unittest
from cipher import *
from string import ascii_lowercase as alphabet
import random

class TestVigenere(unittest.TestCase):
    def test_encrypt_and_decrypt(self):
        def encrypt_and_decrypt(inputs):
            encrypted = [viginere_encrypt(i) for i in inputs]
            decrypted = [viginere_decrypt(i) for i in encrypted]
            return decrypted
            
        trivialinputs = ["",
                         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                         "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
                         "Basic text",
                         alphabet,
                         alphabet.upper()]

        trivialoutputs = encrypt_and_decrypt(trivialinputs)

        trivialinputs = [i.replace(' ', '').lower() for i in trivialinputs]
        for i, j in zip(trivialinputs, trivialoutputs):
            self.assertEqual(i, j)

        
        canyoureplacebasicinput = ["!@#$%^&*()_+",
                                   "0123456789",
                                   "<,>.?:\"'\t\n\r"]

        output = encrypt_and_decrypt(canyoureplacebasicinput)
        for i in output:
            self.assertEqual('', i)

        def gen_random_string():
            random_string = ''
            for _ in range(10000):
                random_string += random.choice(alphabet)
            return random_string

        bunch_of_randoms = [gen_random_string() for _ in range(10)]
        output = encrypt_and_decrypt(bunch_of_randoms)
        for i, j in zip(bunch_of_randoms, output):
            self.assertEqual(i, j)


unittest.main()
