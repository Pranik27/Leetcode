# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:11:11 2020

@author: PRANIKP

Given a string S, return the number of substrings of length K with no repeated characters.

 

Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. 
In this case is not possible to find any substring.

Time Complexity:O(n)
Space Complexity: Constant space
"""

def non_repeating_str(S,k):
    
    if k > len(S):
        return 0
    
    char_count = [0] * 26
    first = 0
    second = 0
    count = 0
    
    while second < len(S):
        
        while second < len(S) and second - first < k:
            
            if char_count[ord(S[second]) - ord('a')] == 0:
                char_count[ord(S[second]) - ord('a')] += 1
                second += 1
            else:
                char_count[ord(S[first]) - ord('a')] -= 1
                first += 1
                
        if second - first == k:
            count += 1
            char_count[ord(S[first]) - ord('a')] -= 1
            first += 1
 
    return count

S = "abcdefklmfnmstuv"
K = 5
print(non_repeating_str(S,K))     
