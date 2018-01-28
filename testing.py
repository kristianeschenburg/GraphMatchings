#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:29:35 2018

@author: kristianeschenburg
"""

import numpy as np

m = np.arange(10).astype(np.int32)
w = np.arange(10).astype(np.int32)

mp = np.zeros((10,10)).astype(np.int32)
wp = np.zeros((10,10)).astype(np.int32)

for h in np.arange(10):
    wp[h,:] = np.random.choice(10,size=(10,),replace=False).astype(np.int32)
    mp[h,:] = np.random.choice(10,size=(10,),replace=False).astype(np.int32) 


import StableMarriage as sm 
    
G = sm.GaleShapely(m,w,mp,wp)
G.marry()