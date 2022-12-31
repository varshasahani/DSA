#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 09:33:02 2022

@author: varsha
"""
def count(s):
    hash={}
    for i in s:
        if i not in hash:
            hash[i]=0
        hash[i]+=1
    arr=[]
    for key,value in hash.items():
        arr.append(value)
    arr.sort(reverse=True)
    count=0
    for i in range(len(arr)):
        if i<9:
            count+=arr[i]
        elif i<18:
            count+=(arr[i]*2)
        else:
            count+=(arr[i]*3)
    return count
s=input()
print(count(s))