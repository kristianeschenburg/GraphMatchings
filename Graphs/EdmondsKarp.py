#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:15:08 2018

@author: kristianeschenburg
"""

class EdmondsKarp(object):
    
    """
    Class to implememnt the Edmonds-Karp algorithm for finding the maximum
    flow in a graph.
    
    Parameters:
    - - - - -
        graph : adjacency matrix representing the directed graph structure.
                    Edges in this graph are weighted by the flow capacity of
                    that edge
    Returns:
    - - - -
        maxFlow : the maximum flow of the graph
    """
    
    