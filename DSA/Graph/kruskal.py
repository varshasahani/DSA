#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 14:15:17 2022

@author: varsha
"""
def krushkal_Mst(graph,nodes):
    graph.sort(key=lambda x:x[2])
    vis=[0]*(nodes+1)
    i=0
    print ("Edge \tWeight")
    while nodes!=1 and i<len(graph):
        x=graph[i][0]
        y=graph[i][1]
        if vis[x]==0 or vis[y]==0:
            vis[x]=1
            vis[y]=1
            print (graph[i][0], "-",graph[i][1], "\t", graph[i][2])
            nodes-=1
        i+=1
        
        
    
nodes,edges=map(int,input().split(" "))
graph=[]
for i in range(edges):
    edge=[int(x) for x in input().split(" ")]
    graph.append(edge)
print("Graph edges")
print(graph)
krushkal_Mst(graph,nodes)
    