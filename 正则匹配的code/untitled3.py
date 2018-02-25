# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:23:13 2018

@author: zhangp
"""
import itertools as its
words = "1234568790abcdefghigklmnopqrstuvwsyzABCDEFGHIGKLMNOPQRSTUVWXYZ"

r =its.product(words,repeat=8)

dic = open("pass.txt","a")

for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))

dic.close()

    
    