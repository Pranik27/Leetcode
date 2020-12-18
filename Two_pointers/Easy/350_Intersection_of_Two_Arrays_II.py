# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:37:23 2020

@author: PRANIKP

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

Time Complexity: O(m + n)
Space Complexity: O(n) , where n is the length of the smallest array.
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        
        if len(nums1) > len(nums2):
            self.intersect(nums2,nums1)
            
        out_list = []
        ht = {}
        
        for i in range(0,len(nums1)):
            if nums1[i] not in ht:
                ht[nums1[i]] = 1
            else:
                ht[nums1[i]] += 1
            
        for i in range(0,len(nums2)):
            
            if ht.get(nums2[i]) > 0:
                out_list.append(nums2[i])
                ht[nums2[i]] -= 1
                
        return out_list
                       
