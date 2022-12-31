#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:16:38 2022

@author: varsha
"""
import sys
from queue import PriorityQueue
def dijsktras(graph,source,nodes,edges):
    vis=[0]*nodes
    ans=[sys.maxsize]*nodes
    ans[0]=0
    pq=PriorityQueue()
    pq.put((0,source))
    
    while not pq.empty():
        node=pq.get()
        #print(node)
        #print(pq)
        vertex=node[1]
        if vis[vertex]:
            continue;
        vis[vertex]=True;
        for child in graph[vertex]:
            cv=child[0]
            cd=child[1]
            if ans[vertex]+cd<ans[cv]:
                ans[cv]=ans[vertex]+cd
                pq.put((ans[cv],cv))

    def printSolution(dist):
            print("Vertex \tDistance from Source")
            for node in range(len(dist)):
                print(node, "\t", dist[node])
    return printSolution(ans)
        
        
    
nodes,edges=map(int,input().split(" "))
graph=[[] for _ in range(nodes)]
for _ in range(edges):
    x,y,w=map(int,input().split(" "))
    graph[x].append([y,w])
    graph[y].append([x,w])
print("Graph",graph)
print(" ")
print(dijsktras(graph,0,nodes,edges))