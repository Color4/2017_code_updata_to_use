# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:50:55 2018

@author: zhangp
"""

import string
letters = string.letters + string.digits + string.punctuation
length = len(letters)
fwrite = open("/genpass.txt","wt")
fread = open("/genpass.txt","r")
for num in xrange(8):
    for times in xrange(length**num):
        line=fread.read(num+1).rstrip()
        for letter in letters:
            fwrite.write(line + letter + "\n")
    fwrite.flush()
fwrite.close()
fread.close()