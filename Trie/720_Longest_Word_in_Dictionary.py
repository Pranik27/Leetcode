# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:15:32 2021

@author: PRANIKP

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].

Time Complexity:O(m*n) + O(nlogn) 
Space Complexity: O(m*n)
"""

class TrieNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.isWordEnd = False


class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        
        curr = self.root
        
        for ch in word:
            
            if (curr.children[ord(ch) - ord('a')] == None):
                curr.children[ord(ch) - ord('a')] = TrieNode()
            
            curr = curr.children[ord(ch) - ord('a')]
        
        curr.isWordEnd = True
    
    def search(self,word):
        
        curr = self.root
        
        for ch in word:
            
            if (curr.children[ord(ch) - ord('a')] == None):
                return False
            
            node = curr.children[ord(ch) - ord('a')]
            if not node.isWordEnd:
                return False
                                 
            curr = curr.children[ord(ch) - ord('a')]
        
        return curr.isWordEnd
            
    

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        tree = Trie()
        max_len = 0
        longet_word = ""
        
        for word in words:
            tree.insert(word)
            
        
        for word in words:
            
            if tree.search(word):
                
                if len(word) == max_len:
                    lex_sort = [longest_word,word]
                    lex_sort.sort()
                    longest_word = lex_sort[0]
                elif len(word) > max_len:
                    longest_word = word
                
                max_len = max(max_len,len(word))
                    
        return longest_word
                