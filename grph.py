#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:23:19 2019

@author: elicandro
"""

def FASTA_parse(file):
    strings={}
    with open(file) as f:
        test=f.read()
        ogg=test.split('>')
    for it in ogg[1:]:
        it=it.split('\n')
        stringid=it.pop(0)
        strings[stringid]=''.join(it)
    return strings

DNA=FASTA_parse("rosalind_grph.txt")

def grph(lst):
    keylist = list(DNA.keys()) 
    vallist = list(DNA.values()) 
    result = ""
    for i in vallist:
        for j in vallist:
            if i[-3:]==j[:3] and i!=j:
                result+=keylist[vallist.index(i)]+' '
                result+=keylist[vallist.index(j)]+'\n'
    return result

with open('rosalind_grph_out.txt', 'w') as f:
    f.write(grph(DNA))