#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:15:08 2018

@author: kristianeschenburg
"""

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
        
        """
        Wrapper method to run Edmonds-Karp algorithm.
        """

        path = traversal.bfs(self.capacity,self.s,self.t)

        while len(path) > 0:

            minFlow = self.pathCapacity(self.capacity,path)

            self.flow = self.updateResiduals(self.capacity,path,minFlow)
            
            self.maxFlow += minFlow
            path = traversal.bfs(self.capacity,self.s,self.t)

    def pathCapacity(self,flowGraph,path):
        
        """
        Compute the minimum flow capacity in the augmenting path.
        
        Parameters:
        - - - - -
            flowGraph : residual on which augmenting path was computed, 
                        with edges weighted by current forward or reverse 
                        flow
            path : augmenting path from source to target node
        """
        
        minFlow = float('inf')
        
        for p in np.arange(len(path)-1):
            minFlow = min(minFlow,flowGraph[path[p],path[p+1]])
        
        return minFlow
    
    def updateResiduals(self,flowGraph,path,minFlow):
        
        """
        Update the residual edges of the flow matrix using the minimum flow
        value of the computed augmenting path.
        
        Parameters:
        - - - - -
            flowGraph : current residual graph
            path : augmenting path
            minFlow : minimum flow capacity of augmenting path
        """
        
        for p in np.arange(len(path)-1):
            flowGraph[path[p],path[p+1]] -= minFlow
            flowGraph[path[p+1],path[p]] += minFlow
        
        return flowGraph