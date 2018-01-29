#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:29:35 2018

@author: kristianeschenburg
"""

import numpy as np

h = np.arange(5).astype(np.int32)
r = np.arange(15).astype(np.int32)

hr = np.zeros((5,15)).astype(np.int32)
rr = np.zeros((15,5)).astype(np.int32)

for hp in np.arange(5):
    hr[hp,:] = np.random.choice(15,size=(15,),replace=False).astype(np.int32)

for rp in np.arange(15):   
    rr[rp,:] = np.random.choice(5,size=(5,),replace=False).astype(np.int32) 
    
positions = np.asarray([3,2,1,2,1])


import GraphMatchings as gm 
    
G = gm.ResidentMatching(h,r,positions,hr,rr)
G.match()