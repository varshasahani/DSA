#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 11:29:07 2022

@author: varsha
"""
from collections import deque
class Solution:
    def isBipartite(graph):
        color=[0]*(len(graph))
        def bipartite(node):
            color[node]=1
            q=deque([node])
            while q:
                cur_node=q.popleft()
                cur_color=color[cur_node]
                for i in graph[cur_node]:
                    if color[i]==cur_color:
                        return False
                    elif color[i]==-cur_color:
                        continue;
                    else:
                        color[i]=-cur_color
                        q.append(i)
            return True
            
        for node in range(len(graph)):
            if color[node]==0:
                if bipartite(node)==False:
                    return False
        return True
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    graph1 = [[1,3],[0,2],[1,3],[0,2]]
    print(isBipartite(graph1))