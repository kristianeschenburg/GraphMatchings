#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:15:08 2018

@author: kristianeschenburg
"""

import copy
import traversal
import numpy as np

class EdmondsKarp(object):
    
    """
    Class to implememnt the Edmonds-Karp algorithm for finding the maximum
    flow in a graph.
    
    Parameters:
    - - - - -
        capacity : graph containing edge capacities
        graph : adjacency matrix representing the directed graph structure
        source : source node
        target : target node
    Returns:
    - - - -
        maxFlow : the maximum flow of the graph
        
    If source == None and target == None, it is assumed that source is the
    first node (index = 0) and target is the last node (index = :end) in the 
    graph array.
    
    """
    
    def __init__(self,capacity,graph,source=None,target=None):
        
        self.capacity = capacity
        self.flow = copy.deepcopy(capacity)
        self.graph = graph
        
        if not source:
            self.s = 0
        else:
            self.s = source
        
        if not target:
            self.t = graph.shape[0]-1
        else:
            self.t = target

        self.maxFlow = 0
        
    def edmondskarp(self):

        path = traversal.bfs(self.flow*self.graph,self.s,self.t)

        while len(path) > 0:
            
            print 'Current Path: {}'.format(path)
            minFlow = self.pathCapacity(self.flow,path)
            
            self.flow = self.updateResiduals(self.flow,path,minFlow)
            
            self.maxFlow += minFlow
            path = traversal.bfs(self.flow*self.graph,self.s,self.t)

    def pathCapacity(self,graph,path):
        
        """
        Compute the minimum weighted edge in a breadth first search path.
        """
        
        minFlow = float('inf')
        
        for i in np.arange(len(path)-1):
            minFlow = min(minFlow,graph[path[i],path[i+1]])
        
        return minFlow
    
    def updateResiduals(self,flow,path,minFlow):
        
        """
        Update the residual edges of the flow matrix.
        """
        
        for p in np.arange(len(path)-1):
            flow[path[p],path[p+1]] = flow[path[p],path[p+1]] - minFlow
            flow[path[p+1],path[p]] = flow[path[p+1],path[p]] + minFlow
        
        return flow