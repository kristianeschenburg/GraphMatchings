#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:41:00 2018

@author: kristianeschenburg
"""

import Queue
import numpy as np

def GaleShapely(object):
    
    """
    Class to apply the Gale-Shapely algorithm to the Stable Marriage problem.
    
    Parameters:
    - - - - -
        men : list of men
        
        women : list of women
        
        male_pref : array of male preferences
        fem_pref : array of female preferences
        
    We assume that men and women are integer valued, starting from 0.

    """
    
    def __init__(self,men,women,male_pref,fem_pref):

        self.male_pref = male_pref
        self.fem_pref = fem_pref
        
        freeMen = Queue.Queue()
        for m in men:
            freeMen.put(m)
        
        proposals_made = np.zeros((len(men),))
        
        male_engaged = np.zeros((len(men),))
        male_engaged[:] = np.nan
        
        fem_engaged = np.zeros((len(women),))
        fem_engaged[:] = np.nan
        
        
    def marry(self,bachelors,proposals,male_spouses,female_spouses):
        
        male_pref = self.male_pref
        fem_pref = self.fem_pref
        
        while not bachelors.empty():
            
            male = bachelors.get()
            pos_spouse = male_pref[proposals[male]]
            
            # if the current woman hasn't yet been proposed to
            # pair this man and woman
            if np.isnan(female_spouses[pos_spouse]):
                
                male_spouses[male] = pos_spouse
                female_spouses[pos_spouse] = male
                
            # if this woman has been proposed to, set her spouse to the one
            # who she prefers, and add the one she doesn't back into the list
            # of eligible bachelors
            else:
                
                if fem_pref[male] > fem_pref[female_spouses[pos_spouse]]:
                    
                    