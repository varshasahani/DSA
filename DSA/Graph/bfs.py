#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:44:40 2022

@author: varsha
"""

def bfs(vertex,graph,vis):
    que=[vertex]
    vis[vertex]=1
    while que:
        node=que.pop(0)
        print(node,end=" ")
        for child in graph[node]:
            
            if vis[child]!=1:
                que.append(child)
                vis[child]=1
            
    
    
nodes,edges=map(int,input().split(" "))
graph=[[] for _ in range(nodes+1)]
vis=[0]*(nodes+1)
for _ in range(edges):
    x,y=map(int,input().split(" "))
    graph[x].append(y)
    graph[y].append(x)
print(graph)
print(bfs(1,graph,vis))