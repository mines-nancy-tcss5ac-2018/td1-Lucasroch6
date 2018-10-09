# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 17:31:52 2018

@author: Lucas
"""

def palindrome(n):
    L1=str(n)
    for i in range (len(L1)):
        if L1[i]==L1[len(L1)-i]:
            return True
        else:
            return False


def reverse(m):
    L2=str(m)
    L3=[]
    for i in range (len(L2)):
        L3.append(L2[len(L2)-i+1])
    return L3[0]

def pb55(n):
    L4=[]
    if n+reverse(n)==palindrome(n):
        L4.append(n)
    return len(L4)

       