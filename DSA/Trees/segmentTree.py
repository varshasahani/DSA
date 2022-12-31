#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:29:24 2022

@author: varsha
"""
import math
def seg(arr,st,i,l,r):
    if l==r:
        st[i]=arr[l]
        return
    mid=(l+r)//2
    seg(arr,st,2*i+1,l,mid)
    seg(arr,st,2*i+2,mid+1,r)
    st[i]=st[2*i+1]+st[2*i+2]
    return
    
def update(si,l,r,i,v):
    if l<=i and i<=r:
        st[si]+=v
        if l==r:
            return
    else:
        return
    mid=(l+r)//2
    update(2*si+1,l,mid,i,v)
    update(2*si+2,mid+1,r,i,v)
    return

def sumRange(si,l,r,x,y):
    if l>=x and r<=y:
        return st[si]
    if r<x or l>y:
        return 0
    mid=(l+r)//2
    return sumRange(2*si+1,l,mid,x,y)+sumRange(2*si+2,mid+1,r,x,y)

    
arr=[int(x) for x in input().split(" ")]
x=math.ceil(math.log2(len(arr)))
st=[0]*(2*(2**x)-1)
print(arr)
seg(arr,st,0,0,len(arr)-1)
print(st)
n=int(input())
for _ in range(n):
    i,v=map(int,input().split(" "))
    v=v-arr[i]
    arr[i]+=v
    update(0,0,len(arr)-1,i,v)
    print(st)

s=int(input())
for _ in range(s):
    x,y=map(int,input().split(" "))
    sm=sumRange(0,0,len(arr)-1,x,y)
    print(sm)