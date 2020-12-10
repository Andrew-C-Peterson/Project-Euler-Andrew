# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 21:44:18 2020

@author: andre
"""


# time module
import time

# time at the start of program execution
start = time.time()


def check_english(ascii1, ascii2):
    """
    function to check if the
    xor(exclusive or) of two ascii
    numbers entered is only letters
    used in common english
    """
    xor = ascii1 ^ ascii2
    if 32<= xor <= 122:
        return True
    return False


def decrypt(s, t):
    """
    This function will take a ascii value and
    a string(the key) and xor with the encrypted text
    and find the real solution
    """
    return ''.join(chr(a ^ ord(b)) for a, b in zip(s, t))

# open the file
f = open('pe059_cipher.txt')

# Strip and split the contents of the file to a list
cipher = f.read().strip().split(',')

# convert the string to integer
cipher = [int(x) for x in cipher]

# letters in ascii from a-z
eng_letters = range(97, 123)

# first letter of the encryption key
first_letter = set([])


# for loop to loop through a-z and cipher text
for j in eng_letters:
    for i in range(0, len(cipher), 3):
        first_letter.add(j)
        if not check_english(cipher[i], j):
            first_letter.remove(j)
            break
        
# second letter of the encryption key
second_letter = set([])

# for loop to loop through a-z and cipher text
for j in eng_letters:
    for i in range(1, len(cipher), 3):
        second_letter.add(j)
        if not check_english(cipher[i], j):
            second_letter.remove(j)
            break

# third character of the encryption key
third_letter = set([])

# for loop to loop through a-z and cipher text
for j in eng_letters:
    for i in range(2, len(cipher), 3):
        third_letter.add(j)
        if not check_english(cipher[i], j):
            third_letter.remove(j)
            break
            
        
#I can't narrow it down any further.. I get multiple possibilities that
#give all english characters, but trial and error reveals the following
        
key = 'exp'
plain_text = ''

# looping through the cipher text
for i in range(0, len(cipher), 3):
    plain_text += decrypt(cipher[i:i+3], key)

print(sum(map(ord, plain_text)))

print(time.time()-start)