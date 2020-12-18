# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:13:41 2020

@author: PRANIKP

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        
        first = 0
        last = 0
        
        char_count = [0] * 26
        max_len = 0
        curr_count = 0
        
        for last in range(len(s)):
            
            
            char_count[ord(s[last]) - ord('A')] += 1
            
            curr_count = max(curr_count,char_count[ord(s[last]) - ord('A')])
            
            while last - first - curr_count + 1 > k:
                
                char_count[ord(s[first]) - ord('A')] -= 1
                first += 1
                
            max_len = max(max_len,last - first + 1)
            
        return max_len

