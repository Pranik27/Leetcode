# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:05:02 2020

@author: PRANIKP

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.

Time Complexity:O(n)
Space Complexity:O(1)
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        first = 0
        last = len(s) - 1
        
        while first < last:
            if s[first].isalnum() and s[last].isalnum():
                if s[first].lower() != s[last].lower():
                    return False
                
                first += 1
                last -= 1
            elif not s[first].isalnum():
                first += 1
            elif not s[last].isalnum():
                last -= 1
                
        return True

