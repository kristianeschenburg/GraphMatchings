#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:41:00 2018

@author: kristianeschenburg
"""

import Queue
import numpy as np

class GaleShapely(object):
    
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
        
        Tests(men,women,male_pref,fem_pref)

        self.male_pref = male_pref
        self.fem_pref = fem_pref
        
        self.bachelors = Queue.Queue()
        for m in men:
            self.bachelors.put(m)
        
        self.proposals = np.zeros((len(men),)).astype(np.int32)
        
        # wives of husband m, and husbands of wife w
        self.wife = {k: np.nan for k in men}
        self.husband = {k: np.nan for k in women}

    def marry(self):
        
        bachelors = self.bachelors

        while not bachelors.empty():

            male = bachelors.get()

            self._propose(male)

        del self.bachelors
        del self.proposals


    def _propose(self,suitor):
        
        """
        Proposal method for single suitor.  Keep proposing until no-longer
        single, or until already proposed to all women.
        """

        engaged = False
        count = self.proposals[suitor]
        preferences = self.male_pref[suitor,:]
        
        while not engaged and count < len(preferences):
            
            partner = preferences[count]
            
            if np.isnan(self.husband[partner]):
                self.wife[suitor] = partner
                self.husband[partner] = suitor
                engaged = True
            else:
                fiancee = self.husband[partner]
                
                if self.fem_pref[partner,suitor] < self.fem_pref[partner,fiancee]:
                    self.bachelors.put(fiancee)
                    self.wife[suitor] = partner
                    self.husband[partner] =  suitor
                    engaged = True
            
            count += 1
        
        self.proposals[suitor] = count
                    
class Tests(object):
    
    """
    Tests to check that inputs to GaleShapley are correct.
    """
    
    def __init__(self,men,women,male_preferences,female_preferences):

        self._testDataType(men,women,male_preferences,female_preferences)
        self._testMemberLength(men,women)
        self._testMemberIdentity(men,women)
        self._testPreferenceShape(male_preferences,female_preferences)
        self._testPreferenceIdentity(male_preferences,female_preferences)
        
    def _testDataType(self,men,women,mp,fp):
        
        assert men.dtype == np.int32
        assert women.dtype == np.int32
        assert mp.dtype == np.int32
        assert fp.dtype == np.int32
        
    def _testMemberLength(self,men,women):
        
        assert len(men) == len(women)
    
    def _testMemberIdentity(self,men,women):
        
        assert len(set(men).symmetric_difference(set(women))) == 0
        
    def _testPreferenceShape(self,mp,fp):

        assert mp.shape == fp.shape
    
    def _testPreferenceIdentity(self,mp,fp):

        assert np.all(np.unique(mp) == np.unique(fp))
            