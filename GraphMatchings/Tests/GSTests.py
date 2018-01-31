#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:37:42 2018

@author: kristianeschenburg
"""

import unittest
import sys
from os.path import dirname,abspath

parent_dir = dirname(dirname(abspath(__file__)))
sys.path.append(parent_dir)

import numpy as np
import GS

class GaleShapleyTestCases(unittest.TestCase):
    
    """
    Tests for GaleShapley graph matching.
    
    Edges cases:
    - - - - -
       1. All men prefer the same women, in the same order
       2. All women prefer the same men in the same order
       3. No male and female preferences align
    """

    def test_simple(self):
        
        """
        A simple 2x2 case, where men's preferences are the same as the women's.
        """

        m = np.asarray([0,1]).astype(np.int32)
        w = np.asarray([0,1]).astype(np.int32)
        
        mp = np.asarray([[0,1],
                         [1,0]]).astype(np.int32)
        wp = np.asarray([[0,1],
                         [1,0]]).astype(np.int32)

        G = GS.GaleShapley(m,w,mp,wp)
        G.marry()
        
        expected = {0:0,
                    1:1}
        
        self.assertTrue(G.husband == expected)
        
    def test_simple_reordered(self):
        
        """
        A simple 2x2 case, where men's preferences are the same as the women's.
        """

        m = np.asarray([1,0]).astype(np.int32)
        w = np.asarray([0,1]).astype(np.int32)
        
        mp = np.asarray([[0,1],
                         [1,0]]).astype(np.int32)
        wp = np.asarray([[0,1],
                         [1,0]]).astype(np.int32)

        G = GS.GaleShapley(m,w,mp,wp)
        G.marry()
        
        expected = {0:0,
                    1:1}
        
        self.assertTrue(G.husband == expected)
        
    def test_shifts(self):
        
        """
        Test shifted case, where men each prefer the next in line.
        """
        
        m = np.asarray([0,1,2,3]).astype(np.int32)
        w = np.asarray([0,1,2,3]).astype(np.int32)
        
        mp = np.asarray([[0,1,2,3],
                         [1,2,3,0],
                         [2,3,0,1],
                         [3,0,1,2]]).astype(np.int32)
    
        wp = np.asarray([[0,1,2,3],
                         [0,1,2,3],
                         [0,1,2,3],
                         [0,1,2,3]]).astype(np.int32)
    
        G = GS.GaleShapley(m,w,mp,wp)
        G.marry()
        
        husbands = {0:0,1:1,2:2,3:3}
        wives = {0:0,1:1,2:2,3:3}
        
        self.assertTrue(G.husband == husbands)
        self.assertTrue(G.wife == wives)
        
    def test_tie_men(self):
        
        """
        Test a case where two men most prefer the same woman.
        """
        
        m = np.asarray([0,1,2]).astype(np.int32)
        w = np.asarray([0,1,2]).astype(np.int32)
        
        mp = np.asarray([[0,1,2],
                         [0,1,2],
                         [0,1,2]]).astype(np.int32)
    
        wp = np.asarray([[0,1,2],
                         [0,1,2],
                         [0,1,2]]).astype(np.int32)
    
        G = GS.GaleShapley(m,w,mp,wp)
        G.marry()
        
        husbands = {0:0,1:1,2:2}
        wives = {0:0,1:1,2:2}
        
        self.assertTrue(G.husband == husbands)
        self.assertTrue(G.wife == wives)

if __name__ == '__main__':

    unittest.main()