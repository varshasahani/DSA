#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:48:49 2022

@author: varsha
"""
def dfs(vertex,graph,vis):
    stack=[vertex]
    vis[vertex]=1
    while stack:
        node=stack.pop()
        print(node,end=" ")
        for child in graph[node]:
            if vis[child]!=1:
                stack.append(child)
                vis[child]=1

                
            
    
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
print("DFS traversal Iterative")
print(dfs(1,graph,vis))




    
    
    
