#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:52:26 2018

@author: kristianeschenburg
"""

from Queue import Queue
import numpy as np

class ResidentMatching(object):
    
    """
    Class to implement a modified version of the Gale-Shapley algorithm for
    a version of the Resident-Hospital Matching problem.  We assume each 
    hospital has h_i spots, and has ranked each applicant from 1:R.  We 
    assume that each resident has ranked all hospitals from 1:H.
    
    Parameters:
    - - - - -
        hospitals : array of hospitals
        residents : array of residents
        positions : number of positions for available at each hospital
        hospital_preferences : array of hospital rankings for each resident
        resident_preferences : array of resident rankings for each hospital
    """
    
    def __init__(self,hospitals,residents,positions,hospital_rankings,
                 resident_rankings):
        
        self.hospitals = hospitals
        self.residents = residents
        
        self.positions = positions
        self.hosp_rank = hospital_rankings
        self.resd_rank = resident_rankings
        
        self.hospOpen = Queue()
        for h in hospitals:
            self.hospOpen.put(h)
            
        self.applied = np.empty((hospitals.shape)).astype(np.int32)
        
        self.hosp_matched = {k: np.zeros((residents.shape)).astype(np.int32) for k in hospitals}
        self.resd_matched = {k: np.nan for k in residents}
        
    def match(self):
        
        hospOpen = self.hospOpen

        while not hospOpen.empty():

            hospital = hospOpen.get()

            self._application(hospital)
            
        [self.hosp_matched,self.unmatched] = self._matchLists()

        del self.hospOpen
        del self.hosp_rank
        del self.resd_rank
        del self.applied
        
    def _application(self,hospital):
        
        """
        Round of applications for a single hospital.
        """
        
        applied = self.applied[hospital] # number of students considered already
        enrolled = self.hosp_matched[hospital].sum()
        rankings = self.hosp_rank[hospital,:] # hospital's rankings of students
        positions = self.positions[hospital] # total positions available

        while applied < len(rankings) and enrolled < positions:
            
            
            
            # get next highest ranked student
            applicant = rankings[applied]
            
            # if this resident is currently unmatched, match them
            if np.isnan(self.resd_matched[applicant]):
                self.hosp_matched[hospital][applicant] = 1
                self.resd_matched[applicant] = hospital
                enrolled += 1
                
            # otherwise, compare resident's preference of their current match
            # to the proposed match
            else:
                
                # current match
                committed = self.resd_matched[applicant]
                
                if self.resd_rank[applicant,hospital] < self.resd_rank[applicant,committed]:

                    self.hospOpen.put(committed)
                    self.resd_matched[applicant] = hospital
                    self.hosp_matched[hospital][applicant] = 1
                    self.hosp_matched[committed][applicant] = 0
                    enrolled += 1
            
            applied += 1

        self.applied[hospital] = applied
        
    def _matchLists(self):
        
        """
        Convert Hospital matchings to dictionaries.
        """
        
        matchings = {k: [] for k in self.hosp_matched.keys()}
        
        matched_residents = set()
        
        for k in matchings:
            residents = list(np.nonzero(self.hosp_matched[k])[0])
            matchings[k] = residents
            matched_residents.update(residents)
        
        unmatched = set(self.residents).difference(set(matched_residents))
        
        return [matchings,unmatched]

        