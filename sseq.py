#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:30:19 2019

@author: elicandro
"""

def sseq(s):
    indices = []
    s=val[0]
    t=val[1]
    a = j = 0
    while a < len(s) and j < len(t):
        if s[a] == t[j]:
            indices.append(a + 1)
            j += 1
        a += 1

    return indices

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

strands=FASTA_parse("rosalind_sseq.txt")
val= list(strands.values())

print(*sseq(strands))