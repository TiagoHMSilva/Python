"""
In cryptography, a Caesar Cipher, also known as an exchange cipher, Caesar code or Caesar exchange, is one of the
simplest and most encryption techniques. It is a type of substitution cipher in which each letter of the text is
replaced by another, which appears in the alphabet below it a fixed number of times.
"""

from functions import *
from time import sleep

while True:
    answer = menu(['Criptografar', 'Descriptografar', 'Exit'])
    if answer == 1:
        encrypt()
    elif answer == 2:
        decrypt()
    elif answer == 3:
        break
    else:
        print('\033[31mERRO: Enter a valid option.\033[m')
    sleep(2)