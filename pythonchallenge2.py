# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 13:42:00 2017
@author: arun
The challenges from 
http://www.pythonchallenge.com/
"""

# Python Challenge 2
# Completed: February 24, 2017
# Problem transferred independently to another project and expanded / continued

inputcode =  "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
outputanswer = ''
# The number of letters by which the alphabet is shifted.
# A = C means keyshift = 2
keyshift = 2

# Two methods
# Method 1
for character in inputcode:
    # if char > a or if char < z
    if (ord(character) >= ord('a') and ord(character) <= ord('z')):
        outputanswer = outputanswer + chr(ord('a') + (ord(character) + keyshift - ord('a'))%26)
    # in this case, simply add the symbol
    else:
        outputanswer = outputanswer + character
print (outputanswer)

# Method 2
# Python alternative using str.maketrans(intab, outtab)
# Completed: May 04, 2016
import string

# Two methods
# Method 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
code = ''
for i in range(0,26):
    code = code + chr(97+(i + keyshift)%26)
    
trantab = str.maketrans(alphabet, code)
print (inputcode.translate(trantab))

# Method 2
table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[keyshift:]+string.ascii_lowercase[:keyshift])
print (str.translate(inputcode, table))
    
# Python Challenge 3

    

