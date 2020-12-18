# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:42:25 2020

@author: PRANIKP
Given a string, find the length of the longest substring T that contains
at most 2 distinct characters.

Example 1
Input: “eceba”
Output: 3
Explanation:
T is "ece" which its length is 3.

Example 2
Input: “aaa”
Output: 3


Time Complexity:O(n)
Space Complexity:Constant Space
"""

def max_substring(s,k):
    
    first = 0
    end = 0
    max_len = 0
    count = 0
    char_count = [0] * 26
    
    for end in range(0,len(s)):
        
        if char_count[ord(s[end]) - ord('a')] == 0:
            count += 1
            char_count[ord(s[end]) - ord('a')] += 1
        else:
            char_count[ord(s[end]) - ord('a')] += 1
            
        if count > k:
            char_count[ord(s[first]) - ord('a')] -= 1
            if char_count[ord(s[first]) - ord('a')] == 0:
                count -= 1
            first += 1
        
        max_len = max(max_len,end - first + 1)
        print(count)
    return max_len
        
        
print(max_substring("ecebax",2))   

