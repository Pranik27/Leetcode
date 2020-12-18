# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:35:54 2020

@author: PRANIKP

Given a linked list, delete N nodes after skipping M nodes of a linked list until the last of the linked list.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the linked list and next M and N respectively space separated. The last line contains the elements of the linked list.

Output:
Function should not print any output to stdin/console.

User Task:
The task is to complete the function linkdelete() which should modify the linked list as required.

Example:
Input:
2
8
2 1
9 1 3 5 9 4 10 1
6
6 1
1 2 3 4 5 6

Output: 
9 1 5 9 10 1
1 2 3 4 5 6

Explanation:
Testcase 1: Deleting one node after skipping the M nodes each time, we have list as 9-> 1-> 5-> 9-> 10-> 1.

Time Complexity: O(n)
Space Complexity: O(1)
"""


'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def skipMdeleteN(head, M, N):
    
    if N == 0:
        return head
    if M == 0:
         return None
    if not head:
        return None
        
    first = head
    last = head
    
    while last and first:
        
        count = 0
        while first and count < M -1:
            first = first.next
            count += 1
        
        count = 0
        
        while last and count < M + N :
            last = last.next
            count += 1
            
        if first:
            first.next = last
            first = first.next
            
    return head
