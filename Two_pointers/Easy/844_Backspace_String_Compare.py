# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:49:45 2020

@author: PRANIKP

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
  
    
        first = len(S) - 1
        second = len(T) - 1
        count = 0
        
        while first >= 0 or second >= 0:
            
            while first >= 0 and (S[first] == '#' or count > 0):
                if S[first] == '#':
                    count += 1
                else:
                    count -= 1
                first -= 1
                
            while second >= 0 and (T[second] == '#' or count > 0):
                if T[second] == '#':
                    count += 1
                else:
                    count -= 1
                second -= 1
                
            if first >= 0 and second >= 0:
                if S[first] == T[second]:
                    first -= 1
                    second -= 1
                else:
                    return False
            else:
                if first >= 0 or second >= 0:
                    return False

            
        return True
