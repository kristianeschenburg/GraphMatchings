#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:37:42 2018

@author: kristianeschenburg
"""

import numpy as np
import unittest
import GraphMatchings as gm

class GaleShapleyTestCases(unittest.TestCase):
    
    """
    Tests for GaleShapley graph matching.
    """
    
    def simple(self):
        
        """
        A simple 2x2 case, where men's preferences are the same as the women's.
        """
        
        m = np.asarray([1,0]).astype(np.int32)
        w = np.asarray([0,1]).astype(np.int32)
        
        mp = np.asarray([[0,1],[1,0]]).astype(np.int32)
        wp = np.asarray([[0,1],[1,0]]).astype(np.int32)
        
        G = gm.GaleShapley(m,w,mp,wp)
        
        self.assertTrue(G.husbands == {0:0,1:1})

if __name__ == 'main':
    unittest.main()