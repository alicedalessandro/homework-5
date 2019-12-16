#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:37:12 2019

@author: elicandro
"""

from itertools import permutations

def perm(n):
    totp=0
    l1=list(permutations(range(1,n+1)))
    l2=[]
    string=''
    for i in l1:
        totp+=l1.count(i)
    l2.append(str(totp))
    for i in l1:
        for j in i:
            string+=str(j)
        l2.append(string)
        string=''
    return l2


with open('rosalind_perm_out.txt', 'w') as f:
    arr=perm(5)
    f.write(arr[0] + '\n')
    del arr[0]
    for j in arr:
        j=' '.join(j)
        f.write(j + '\n')