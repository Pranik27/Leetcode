# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 02:10:39 2020

@author: PRANIKP

Given an array of 0’s and 1’s, we need to write a program to 
find the minimum number of swaps required to group all 1’s present in the array together.

Input : arr[] = {1, 0, 1, 0, 1}
Output : 1
Explanation: Only 1 swap is required to 
group all 1's together. Swapping index 1
and 4 will give arr[] = {1, 1, 1, 0, 0}

Input : arr[] = {1, 0, 1, 0, 1, 1}
Output : 1

Time Complexity: O(n)
Space Complexity:O(1)
"""

def min_swap(A):
    
    start = 0
    end = len(A) - 1
    count = 0
    
    while start < end:
        
        while A[start] != 1:
            start += 1
            
        if A[end] == 0:
            A[start],A[end] = A[end],A[start]
            start += 1
            end -= 1
            count += 1
        else:
            end -= 1
            
            
    return count

A = [1, 0, 1, 0, 1, 1, 1, 1, 0,1]
print(min_swap(A))
            
        
    
    

