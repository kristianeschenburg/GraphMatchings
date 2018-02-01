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
    National Resident Matching problem.  We assume each hospital has p_h 
    positions available, and has ranked each applicant from 1:R.  We assume 
    that each resident has ranked all hospitals from 1:H.
    
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
        self.h_rank = hospital_rankings
        self.r_rank = resident_rankings
        
        # initialize queue of hospitals
        self.open_hospitals = Queue()
        for h in hospitals:
            self.open_hospitals.put(h)
            
        # number of applicants each hospital has considered so far
        self.applied = np.empty((hospitals.shape)).astype(np.int32)
        
        # current H-->R and R-->H matchings
        self.h_matched = {k: np.zeros((residents.shape)).astype(np.int32) for k in hospitals}
        self.r_matched = {k: np.nan for k in residents}
        
    def match(self):
        
        """
        NRM wrapper method.
        """
        
        open_hospitals = self.open_hospitals

        while not open_hospitals.empty():

            hospital = open_hospitals.get()

            self._application(hospital)
            
        [self.h_matched,self.unmatched] = self._matchLists()

        del self.open_hospitals
        del self.h_rank
        del self.r_rank
        del self.applied
        
    def _application(self,hospital):
        
        """
        Matching method for a single hospital.  Consider applicants until all
        available positions are filled, or until all residents have been 
        considered.
        
        Parameters:
        - - - - -
            hospital : single hospital identifier
        """
        
        # number of residents considered already
        applied = self.applied[hospital]
        # current number of matched residents
        enrolled = self.h_matched[hospital].sum()
        # hospital's ranking of students
        rankings = self.h_rank[hospital,:]
        # total number of positions available at hospital
        positions = self.positions[hospital]

        # while hospital has not yet considered all students AND while 
        # current number of matched students is less than avail. positions
        while applied < len(rankings) and enrolled < positions:

            # get next highest ranked student
            applicant = rankings[applied]
            
            # if this resident is currently unmatched, match them
            if np.isnan(self.r_matched[applicant]):
                self.h_matched[hospital][applicant] = 1
                self.r_matched[applicant] = hospital
                enrolled += 1
                
            # otherwise, compare resident's preference of their current match
            # to the proposed match
            else:
                
                # current match
                committed = self.r_matched[applicant]
                
                # if new proposed hospital is ranked higher by resident
                # than current match
                if self.r_rank[applicant,hospital] < self.r_rank[applicant,committed]:

                    self.open_hospitals.put(committed)
                    self.r_matched[applicant] = hospital
                    self.h_matched[hospital][applicant] = 1
                    self.h_matched[committed][applicant] = 0
                    enrolled += 1

            applied += 1

        self.applied[hospital] = applied
        
    def _matchLists(self):
        
        """
        Convert hospital matchings to dictionary structure and determine
        which residents were not matched to a hospital.
        """
        
        matchings = {k: [] for k in self.h_matched.keys()}
        
        matched_residents = set()
        
        for k in matchings:
            residents = list(np.nonzero(self.h_matched[k])[0])
            matchings[k] = residents
            matched_residents.update(residents)
        
        unmatched = set(self.residents).difference(set(matched_residents))
        
        return [matchings,unmatched]

        