# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:46:24 2021

@author: PRANIKP

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

Time Complexity: O(logn)
Space Complexity:O(n)
"""

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
    
    def top(self,heap):
        return heap[0]
    
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.max_heap or -self.top(self.max_heap) > num:
            heapq.heappush(self.max_heap,-num)
        else:
            heapq.heappush(self.min_heap,num)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        
        if len(self.max_heap) == len(self.min_heap):
            return float((float(-self.top(self.max_heap)) + float(self.top(self.min_heap)))/2)
        else:
            if len(self.min_heap) > len(self.max_heap):
                return  float(self.top(self.min_heap))
            else:
                return float(-self.top(self.max_heap))


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()