#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:41:00 2018

@author: kristianeschenburg
"""

from Queue import Queue
import numpy as np

class GaleShapley(object):
    
    """
    Class to apply the Gale-Shapley algorithm to the Stable Marriage 
    problem.  Assumes that it class will receive a list of N men, and N women, 
    where each man and each woman have ranked all members of the opposite sex, 
    with rankings contained in NxN arrays.
    
    Parameters:
    - - - - -
        men : array of men
        women : array of women
        male_pref : array of male preferences (NxN)
        fem_pref : array of female preferences (NxN)
        
    We assume that men and women are integer valued, starting from 0.

    """
    
    def __init__(self,men,women,male_pref,fem_pref):
        
        # Check data types, and check tests
        men = men.astype(np.int32)
        women = women.astype(np.int32)
        male_pref = male_pref.astype(np.int32)
        fem_pref = fem_pref.astype(np.int32)
        
        DataChecks(men,women,male_pref,fem_pref)

        # initialize attributes
        self.male_pref = male_pref
        self.fem_pref =  fem_pref
        
        self.bachelors = Queue()
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
                    
class DataChecks(object):
    
    """
    Tests to check that inputs to GaleShapley are correct.
    """
    
    def __init__(self,men,women,male_preferences,female_preferences):

        self._testMemberLength(men,women)
        self._testMemberIdentity(men,women)
        self._testPreferenceShape(male_preferences,female_preferences)
        self._testPreferenceIdentity(male_preferences,female_preferences)

    def _testMemberLength(self,men,women):
        
        try:
            len(men) == len(women)
        except:
            raise AssertionError
    
    def _testMemberIdentity(self,men,women):
        
        try:
            len(set(men).symmetric_difference(set(women))) == 0
        except:
            raise AssertionError
    
    def _testPreferenceShape(self,mp,fp):

        try:
            mp.shape == fp.shape
        except:
            raise AssertionError
    
    def _testPreferenceIdentity(self,mp,fp):

        try:
            np.all(np.unique(mp) == np.unique(fp))
        except:
            raise AssertionError
            