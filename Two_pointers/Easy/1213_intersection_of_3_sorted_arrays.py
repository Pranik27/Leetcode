# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:53:14 2020

@author: PRANIKP

Given three arrays sorted in non-decreasing order, 
print all common elements in these arrays.

Input:
ar1[] = {1, 5, 10, 20, 40, 80}
ar2[] = {6, 7, 20, 80, 100}
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20, 80

Input:
ar1[] = {1, 5, 5}
ar2[] = {3, 4, 5, 5, 10}
ar3[] = {5, 5, 10, 20}
Output: 5, 5

Time Complexity:O(n1 + n2 + n3) 
Space Complexity: O(n) where n is the length of the longest array
"""


def find_common(arr1,arr2,arr3):
    
    if len(arr1) == 0 or len(arr2) == 0 or len(arr3) == 0:
        return 0
    
    first = 0
    second = 0
    third = 0
    out_list = []
    
    while first < len(arr1) and second < len(arr2) and third < len(arr3):
        
        if arr1[first] == arr2[second] and arr2[second] == arr3[third]:
            out_list.append(arr1[first])
            first += 1
            second += 1
            third += 1
        elif arr1[first] < arr2[second]:
            first += 1
        elif arr1[first] > arr2[second]:
            second += 1
        else:
            third += 1
            
    
    return out_list

ar1 = [1, 5, 5]
ar2 = [3, 4, 5, 5, 10]
ar3 = [5, 5, 10, 20]
print(find_common(ar1,ar2,ar3))
        
        