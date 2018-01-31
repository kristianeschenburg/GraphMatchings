#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:29:35 2018

@author: kristianeschenburg
"""

import numpy as np

"""
h = np.arange(5).astype(np.int32)
r = np.arange(15).astype(np.int32)

hr = np.zeros((5,15)).astype(np.int32)
rr = np.zeros((15,5)).astype(np.int32)

for hp in np.arange(5):
    hr[hp,:] = np.random.choice(15,size=(15,),replace=False).astype(np.int32)

for rp in np.arange(15):   
    rr[rp,:] = np.random.choice(5,size=(5,),replace=False).astype(np.int32) 
    
positions = np.asarray([3,2,1,2,1])
"""

m = np.asarray([0,1]).astype(np.int32)
w = np.asarray([0,1]).astype(np.int32)

mp = np.asarray([[0,1],
                 [1,0]]).astype(np.int32)
wp = np.asarray([[0,1],
                 [1,0]]).astype(np.int32)

import GraphMatchings as gm 
    
#G = gm.ResidentMatching(h,r,positions,hr,rr)
#G.match()

G = gm.GaleShapely(m,w,mp,wp)
G.marry()