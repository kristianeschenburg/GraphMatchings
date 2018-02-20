#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 02:21:22 2018

@author: kristianeschenburg
"""

import numpy as np

class Graph(object):
    
    """
    Class to construct a graph object from an adjacency list or adjacency
    matrix.
    """
    
    def __init__(self,directed=False):
        
        self.directed = directed
        self.numNodes = 0
        self.nodes = {}
    
    def add_node(self,node):
        
        """
        Method to add node to a list of nodes.
        """
        
        vertex = Vertex(node)
        
        self.nodes[node] = vertex
        self.numNodes += 1
    
    def add_edge(self,source,target,weight):
        
        """
        Method to add an edge to a list of edges.
        """
        
        # Check if source exists already
        if source not in self.nodes.keys():
            self.add_node(source)
        if target not in self.nodes.keys():
            self.add_node(target)
        
        # Add target to adjacent nodes of source
        # If graph is not directed, add source to adjacent nodes of target
        self.nodes[source].add_neighbor(self.nodes[target])
        if not self.directed:
            self.nodes[target].add_neighbor(self.nodes[source])
            
class Vertex(object):
    
    """
    Class to construct a vertex object.
    
    Parameters:
    - - - - -
        name : vertex ID
        properties : dictionary of properties describing vertex.  For example,
                        {'density': 10}
    """
    
    def __init__(self,name,properties=None,adjacent=None):
        
        self.name = name
        self.properties = properties
        self.adjacent = adjacent

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def properties(self):
        return self.__properties
    
    @properties.setter
    def properties(self,properties):
        if properties:
            for k,v in properties.items():
                self.__properties.update({k:v})
        else:
            self.__properties = {}

    def add_neighbor(self,neighbor,weight=1):
        
        """
        Method to add neighbor to vertex.
        
        Parameters:
        - - - - -
            neighbor : ID of neighbor vertex
            weight : weight of edge from self to neighbor
        """
        
        self.adjacent.update({neighbor: weight})
        
    def get_neighbors(self):
        
        """
        Get neighboring vertices of self.
        """
        
        return self.adjacent.keys()
        
    def get_weight(self,neighbor):
        
        """
        Get weight of edge between self and neighbor.
        
        Parameters:
        - - - - -
            neighbor : ID of neighbor vertex
        """
        
        return self.adjacent[neighbor]


def from_array(graph,directed=False):
    
    """
    Method to generate a Graph object from a numpy adjacency matrix.
    
    Parameters:
    - - - - -
        graph : adjacency matrix.  Index i,j /= 0 indicates that vertices i 
                    and j are neighbors in the graph, where is edge weight
                    is indicated by the value.
        directed : boolean indicating whether graph is directed or undirected
    """
    
    G = Graph()
    
    [x,y] = graph.shape
    added = np.zeros((graph.shape[0],))
    
    for ns in np.arange(x):
        for nt in np.arange(y):
            
            if graph[ns,nt]:
                
                source = Vertex(ns)
                target = Vertex(nt)
                weight = graph[ns,nt]
                
                source.add_neighbor(target,weight)
                
                if not added[ns]:
                    G.add_node(source)
                    added[ns] = 1
                    
                if not added[nt]:
                    G.add_node(target)
                    added[nt] = 1

    return G

def from_dict_of_lists(graph,directed=False):
    
    """
    Method to generate a Graph object from an adjancey list structure.
    
    Parameters:
    - - - - -
        graph : adjacency list, represented by a dictionary of lists
        directed : boolean indicating whether graph is directed or undirected
    """