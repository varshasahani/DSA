#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:34:14 2022

@author: varsha
"""
import sys

def print_mst(parent,dis):
    print ("Edge \tWeight")
    for i in range(2,len(parent)):
        print (parent[i], "-", i, "\t", dis[i])

def minm(vis,source):
    mn=sys.maxsize
    node=source
    for edge in graph[source]:
            if edge[1]<mn and vis[edge[0]]!=1:
                node=edge[0]
                mn=edge[1]
    edge=[node,mn]
    return edge
    

def prims_mst(source,graph,vis,nodes):
    vis[source]=1
    dis[source]=0
    parent[source]=-1
    relax=nodes-1
    nodes=[source]
    while relax!=0:
        mn=sys.maxsize
        for node in nodes:
            edge=minm(vis,node)
            if edge[1]<mn:
                mn=edge[1]
                nx_node=edge[0]
                pr=node
        vis[nx_node]=1
        dis[nx_node]=mn
        nodes.append(nx_node)
        parent[nx_node]=pr
        relax-=1
        
    
    return print_mst(parent,dis)

nodes,edges=map(int,input().split(" "))
graph=[[] for _ in range(nodes+1)]
vis=[0]*(nodes+1)
dis=[sys.mmaxsize]*(nodes+1)
parent=[0]*(nodes+1)
for _ in range(edges):
    x,y,wt=map(int,input().split(" "))
    graph[x].append([y,wt])
    graph[y].append([x,wt])
print("Given graph In Adjucency List")
print(graph)
print("")
print("Prims Minimum Spanning Tree")
prims_mst(1,graph,vis,nodes)
