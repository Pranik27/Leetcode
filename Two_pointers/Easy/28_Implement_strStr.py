# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:06:57 2020

@author: PRANIKP

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
 

Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.

Time Complexity: O(m+n)
Space Complexity:O(n)
"""


class Solution(object):
    
    def calLPS(self,arr):
        
        res = [0] * len(arr)
        
        p1 = 0
        p2 = 1
        
        while p2 < len(arr):
            if arr[p2] == arr[p1]:
                res[p2] = p1 + 1 
                p2 += 1
                p1 += 1
            else:
                if p1 !=0:
                    p1 = res[p1 - 1]
                else:
                    res[p2] = 0
                    p2 += 1
        
        return res
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        first = 0
        second = 0
        
        lps = [0] * len(needle)
        
        lps = self.calLPS(needle)
        
        while first < len(haystack):
            
            if haystack[first] == needle[second]:
                first += 1
                second += 1
            else:
                if second != 0:
                    second = lps[second - 1]
                else:
                    first += 1
                    
            if second == len(needle):
                return first - second
            
        return -1
