# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:36:58 2021

@author: PRANIKP

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

Time Complexity: O(n) , where n is the no of words.
Space Complexity: Constant Space
"""

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        alien_dict = {}
        count = 0 
        
        for ch in order:
            alien_dict[ch] = count
            count += 1
        
        for idx in range(0,len(words) - 1):
            
            word1 = words[idx]
            word2 = words[idx + 1]
            
            for x in range(0,min(len(word1),len(word2))):
                
                if word1[x] != word2[x]:
                    if alien_dict[word1[x]] > alien_dict[word2[x]]:
                        return False
                    break
            else:
                    if len(word1) > len(word2):
                        return False
            
        return True

