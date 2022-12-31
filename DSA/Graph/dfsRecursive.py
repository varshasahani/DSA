#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:32:45 2022

@author: varsha
"""

def dfs2(vertex,graph,vis):
    vis[vertex]=1
    print(vertex,end=" ")
    
    for child in graph[vertex]:
        if vis[child]!=1:
            vis[child]=1
            dfs2(child,graph,vis)
nodes,edges=map(int,input().split(" "))
graph=[[] for _ in range(nodes+1)]
vis=[0]*(nodes+1)

for _ in range(edges):
    x,y=map(int,input().split(" "))
    graph[x].append(y)
    graph[y].append(x)
print("Given graph")
print(graph)
print("")
print("DFS traversal Recursive")
print(dfs2(1,graph,vis))