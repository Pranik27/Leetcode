# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 21:42:07 2021

@author: PRANIKP

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        out_list = []
        start = 0
        end = 0
        
        char_last_idx = [0] * 26
        
        for x,y in enumerate(S):
            char_last_idx[ord(y) - ord('a')] = x
            
        for i in range(0,len(S)):
            
            end = max(end,char_last_idx[ord(S[i]) - ord('a')])

            if i == end:
                out_list.append(end - start + 1)
                start = end + 1

        return out_list
        