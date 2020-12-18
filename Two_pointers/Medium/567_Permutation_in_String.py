# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:15:22 2020

@author: PRANIKP

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    
    def matches(self,arr1,arr2):
        
        for index in range(0,len(arr1)):
            if arr1[index] != arr2[index]:
                return False
            
        return True
    
    
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        char_count1 = [0] * 26
        char_count2 = [0] * 26
        first = 0
        last = 0
        
        
        while last < len(s1):
            
            char_count1[ord(s1[last]) - ord('a')] += 1
            char_count2[ord(s2[last]) - ord('a')] += 1
            last += 1
        
        last -= 1
        
        while last < len(s2):
            
            if (self.matches(char_count1,char_count2)):
                return True
            
            char_count2[ord(s2[first]) - ord('a')] -= 1
            first += 1
            last += 1
            if last < len(s2):
                char_count2[ord(s2[last]) - ord('a')] += 1
                
        return False
                

