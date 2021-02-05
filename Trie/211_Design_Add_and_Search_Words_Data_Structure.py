# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 00:23:45 2021

@author: PRANIKP

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.

Time Complexity: O(m*n)
Space Complexity:O(m*n)
where m and n are the no of words and n is the lenght of each word respectively.
"""

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.isWordEnd = False
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self
        
        for ch in word:
            
            node = curr.children.get(ch)
            if not node:
                node = WordDictionary()
                curr.children.update({ch:node})
            
            curr = node
        
        curr.isWordEnd = True    
        

    def match(self,word,idx,node):
        
        if not node:
            return False
        
        if idx == len(word):
            return node.isWordEnd
        
        if word[idx] == ".":
            
            for child_node in node.children.values():
                
                if self.match(word,idx + 1, child_node):
                    return True
            return False
        else:
            curr = node.children.get(word[idx])
            
            if not curr:
                return False
            
            return self.match(word,idx + 1,curr)
            
        
    
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self
        
        return self.match(word,0,curr)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)