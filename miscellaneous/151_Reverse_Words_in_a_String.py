# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:41:04 2021

@author: PRANIKP

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow up:

Could you solve it in-place with O(1) extra space?

Time Complexity:O(n)
Space Complexity:O(n)
"""

class Solution(object):
    
    def trimSpaces(self,s):
        
        left = 0
        right = len(s) - 1
        
        while left < right and s[left] == ' ':
            left += 1
            
        while right > left and s[right] == ' ':
            right -= 1
        
        out = []
        
        for idx in range(left,right + 1):
            
            if s[left] != ' ':
                out.append(s[left])
            elif out[-1] != ' ':
                out.append(s[left])
            
            left += 1
        
        return out
    
    def reverse(self, l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
    
    def reverse_each_word(self, l):
        n = len(l)
        start = end = 0
        
        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1
        
        
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        l = self.trimSpaces(s)
        l.reverse()
        
        self.reverse_each_word(l)
        
        
        return ''.join(l)
        

