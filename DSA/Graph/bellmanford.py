#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 22:15:48 2022

@author: varsha
"""
import sys
def printPath(parent,dis):
    print ("Edge \tShortest-path")
    for i in range(len(parent)-1):
        print (parent[i], "-", i, "\t", dis[i])
        
def bellmanFord(graph,nodes):
    parent=[0]*(nodes+1)
    dis=[sys.maxsize]*(nodes+1)
    dis[0]=0
    relax=nodes-1
    while relax!=0:
        updated=0
        for edge in graph:
            x=edge[0]
            y=edge[1]
            wt=edge[2]
            if dis[x]+wt<dis[y]:
                dis[y]=dis[x]+wt
                updated=1
                parent[y]=x
        if updated==0:
            break;
        relax-=1
    if updated==1:
        for edge in graph:
            x=edge[0]
            y=edge[1]
            wt=edge[2]
            if dis[x]+wt<dis[y]:
                dis[y]=dis[x]+wt
                updated=1
                parent[y]=x
    if updated==1:
        print("Graph contains negative weight cycle")
    else:
        print(printPath(parent,dis))
    
        
            
nodes,edges=map(int,input().split(" "))
graph=[]
for _ in range(edges):
    edge=[int(x) for x in input().split(" ")]
    graph.append(edge)
print("edges of graph")
print(graph)
bellmanFord(graph,nodes)