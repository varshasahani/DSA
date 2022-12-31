#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:05:20 2022

@author: varsha
"""

def knapSack(W, wt, val, n):
 
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
 
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
 
    
val = [45, 100, 20,56]
wt = [10, 20, 30,40]
W = 50
n = len(val)
print(val)
print(wt)
print(knapSack(W, wt, val, n))