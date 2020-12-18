# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:54:50 2020

@author: PRANIKP

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

Time Complexity: O(n)
Space Complexity: constant space
"""

class Solution(object):
    def reverseVowels(self, S):
        """
        :type s: str
        :rtype: str
        """
        vow = ['a','e','i','o','u','A','E','I','O','U']
        S = list(S)
        first = 0
        last = len(S) - 1
        
        while first < last:
            
            if S[first] in vow and S[last] in vow:
                S[first],S[last] = S[last],S[first]
                first += 1
                last -= 1
            elif S[first] not in vow:
                first += 1
            elif S[last] not in vow:
                last -= 1
                
        return "".join(S)

