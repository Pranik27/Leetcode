# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:17:03 2020

@author: PRANIKP

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_set = set()
        first = 0
        end = 0
        max_len = 0
        
        while end < len(s):
            
            while end < len(s) and s[end] not in new_set:
                new_set.add(s[end])
                end += 1
            
            max_len = max(max_len,len(new_set))
            new_set.discard(s[first])
            first += 1
            
        return max_len
        

