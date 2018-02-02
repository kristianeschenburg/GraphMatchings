#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:20:04 2018

@author: kristianeschenburg
"""

from Queue import Queue
import numpy as np

def bfs(graph,s,t):
    
    """
    Breadth First Search from source vertex s to target vertex t.  Returns the
    final path.  If there is no path, list will be empty.
    
    Parameters:
    - - - - -
        graph : directed adjacency matrix, where rows are source nodes of
                an edge, and columns are target nodes of an edge
        s : source node from which to search for a path
        t : target node to which to search for path
    """
    
    visited = np.zeros((graph.shape[0],)).astype(np.int32)
    parent = -1 * np.ones((graph.shape[0],)).astype(np.int32)
    
    Q = Queue()
    Q.put(s)

    while not Q.empty():
        
        vertex = Q.get()

        for n in np.arange(graph.shape[1]):
            if not visited[n] and graph[vertex][n]:
                
                parent[n] = vertex
                
                if n == t:
                    
                    return parent,visited

                Q.put(n)

        visited[vertex] = 1
    
    return parent,visited

def path(parents,t):
    
    """
    Build path from source to target.
    
    Parameters:
    - - - - -
        parents : array, where each index [i] points to the parent node of
                    node i
        t : node from which to traverse backwards
    """
    path_stack = []
    path_stack.append(t)
    
    while parents[t] != -1:
        path_stack.append(parents[t])
        t = parents[t]

    path = []
    while len(path_stack) != 0:
        path.append(path_stack.pop())
        
    return path