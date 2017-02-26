# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 13:42:00 2017
@author: arun
The challenges from 
http://www.pythonchallenge.com/
"""

# Python Challenge 1
# Completed: February 24, 2017
# Problem transferred independently to another project and expanded / continued

# Two methods
# Method 1
def caesar_cipher1(inputcode, keyshift):
    outputanswer = ''
    for character in inputcode:
        # if char > a or if char < z
        if (ord(character) >= ord('a') and ord(character) <= ord('z')):
            outputanswer = outputanswer + chr(ord('a') + (ord(character) + keyshift - ord('a'))%26)
        # in this case, simply add the symbol
        else:
            outputanswer = outputanswer + character
    return outputanswer   


# Method 2
# Python alternative using str.maketrans(intab, outtab)
# Two methods
# Method 2.1
def caesar_cipher2_1(inputcode, keyshift):    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    code = ''
    for i in range(0,26):
        code = code + chr(97+(i + keyshift)%26)    
    trantab = str.maketrans(alphabet, code)
    return (inputcode.translate(trantab))

# Method 2.2
def caesar_cipher2_2(inputcode, keyshift):
    import string
    table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[keyshift:]+string.ascii_lowercase[:keyshift])
    return (str.translate(inputcode, table))

# given cipher
inputcode =  "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
# The number of letters by which the alphabet is shifted.
keyshift = 2 # A = C means keyshift = 2

print (caesar_cipher1(inputcode, keyshift))
print (caesar_cipher2_1(inputcode, keyshift))
print (caesar_cipher2_2(inputcode, keyshift))

# applying on url
inputcode = "map"
keyshift = 2
print (caesar_cipher1(inputcode, keyshift))
print (caesar_cipher2_1(inputcode, keyshift))
print (caesar_cipher2_2(inputcode, keyshift)) 

