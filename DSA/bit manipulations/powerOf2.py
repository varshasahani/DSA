#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:44:41 2022

@author: varsha
"""

def powerOf2(n):
    if n==0:
        return 0
    if n&(~(n-1))==n:
        return 1
    return 0

n=int(input())
print(powerOf2(n))
            