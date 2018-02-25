# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:39:50 2018

@author: zhangp
"""

import Levenshtein

one_list = []
two_list = []


with open('file.txt', 'rb') as input_data:
    #input_data.readline()
    input_data.readline()
    line_all = input_data.readlines()
    for line_one in line_all:
        #print(line_one)
        line = line_one.rstrip().split('\t'.encode(encoding='utf-8'))
        one_data = line[0]
        if len(line[0]) == 0:
            one_data = 'NNNNNNNNNNN'
            two_data = 'NNNNNNNNNNN'
        if str(line[0]).find('N')!=-1:
            one_data = 'NNNNNNNNNNN'
        if len(line)==1:
            two_data = 'NNNNNNNNNNN'
        else:
            if str(line[0]).find('N')!=-1:
                two_data = 'NNNNNNNNNNN'
            if line[1] == 0:
                two_data = 'NNNNNNNNNNN'
        #print(line)
        #print(line[0])
        #print(line[1])
        #one_list.append(line[0])
        #two_list.append(line[1])
        one_list.append(one_data)
        two_list.append(two_data)

for i in range(1,len(one_list)):
    for j in range(i+1,len(one_list)):
        A_one_list = str(one_list[i])[2:len(str(one_list[i]))-1]
        B_one_list = str(one_list[j])[2:len(str(one_list[j]))-1]
        A_two_list = str(two_list[i])[2:len(str(two_list[i]))-1]
        B_two_list = str(two_list[j])[2:len(str(two_list[j]))-1]
        if A_one_list =='MID':
            A_one_list = 'NNNNNNN'
        if B_one_list =='MID':
            B_one_list = 'NNNNNNN'
        if B_two_list =='MID':
            B_two_list = 'NNNNNNN'
        if A_two_list =='MID':
            A_two_list = 'NNNNNNN'
        #print(len(A_one_list))
        #print(len(B_one_list))
        if len(A_one_list)==7 or len(B_one_list)==7:
            B_one_list = B_one_list[0:7]
            A_one_list = A_one_list[0:7]
        #print(i)
        #print(j)
        #print(A_one_list)
        #print(B_one_list)
        if(Levenshtein.hamming(A_one_list, B_one_list)==0):
            #print(A_two_list)
            if A_two_list=='NNNNNNN' or A_two_list=='NNNNNNN':
                print(A_one_list)
                print(B_one_list)
                print('%s and %s same'%(i+2,j+2))
            else:
                if len(A_two_list)==7 or len(B_two_list)==7:
                    B_two_list = B_two_list[0:6]
                    A_two_list = A_two_list[0:6]
                if Levenshtein.hamming(A_two_list, B_two_list)==0:
                    print('%s and %s same'%(i+2,j+2))
                    print(A_one_list)
                    print(B_one_list)
                if Levenshtein.hamming(A_two_list, B_two_list)==1:
                    print('%s and %s most same by one word'%(i+2,j+2))
                    print(A_one_list)
                    print(B_one_list)
        if(Levenshtein.hamming(A_one_list, B_one_list)==1):
            #print(A_two_list)
            if A_two_list=='NNNNNNN' or A_two_list=='NNNNNNN':
                print(A_one_list)
                print(B_one_list)
                print('%s and %s most same by one word'%(i+2,j+2))
            else:
                if len(A_two_list)==7 or len(B_two_list)==7:
                    B_two_list = B_two_list[0:6]
                    A_two_list = A_two_list[0:6]
                if Levenshtein.hamming(A_two_list, B_two_list)==0:
                    print('%s and %s same by one word'%(i+2,j+2))
                    print(A_one_list)
                    print(B_one_list)
                if Levenshtein.hamming(A_two_list, B_two_list)==1:
                    print('%s and %s most same by two word'%(i+2,j+2))
                    print(A_one_list)
                    print(B_one_list)
                #print(Levenshtein.hamming(A_one_list, B_one_list))
                #print(A_one_list)
                #print(B_one_list)           
                #print(A_two_list)
                #print(B_two_list)
     
#print(one_list)

#print(Levenshtein.hamming(one_list[3], one_list[2]))


