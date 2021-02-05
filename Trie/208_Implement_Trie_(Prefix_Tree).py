# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:27:07 2021

@author: PRANIKP

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

Time Complexity: 
Insert: O(m*n) 
Search: O(n) 
StartsWith: O(n)
where m is the no of words and n is the length of each word respectively

Space Complexity:
Insert: O(26*m*n)
Search: O(1)
StartsWith: O(1)
where m is the no of words and n is the length of each word respectively
"""

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.isWordEnd = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        
        curr = self
        for ch in word:
            
            if curr.children[ord(ch) - ord('a')] == None:
                curr.children[ord(ch) - ord('a')] = Trie()
            
            curr = curr.children[ord(ch) - ord('a')]
        
        curr.isWordEnd = True
                
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        curr = self
        
        for ch in word:
            
            if not curr.children[ord(ch) - ord('a')]:
                return False
            
            curr = curr.children[ord(ch) - ord('a')]

        return curr.isWordEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self
        
        for ch in prefix:
            
            if not curr.children[ord(ch) - ord('a')]:
                return False
            
            curr = curr.children[ord(ch) - ord('a')]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)