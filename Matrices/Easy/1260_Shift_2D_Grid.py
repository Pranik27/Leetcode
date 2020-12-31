# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:46:04 2020

@author: PRANIKP

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

 

Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:


Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100

Time Complexity: O(m*n)
Space Complexity:O(m*n)
"""

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return grid
        
        row_length = len(grid)
        col_length = len(grid[0])
        temp = []
        
        k = k % (row_length * col_length)
        
        for _ in grid:
            
            temp.extend(_)
        
        temp = temp[-k:] + temp[:-k]
        idx = 0
        
        for x in range(row_length):
            
            for y in range(col_length):
                
                grid[x][y] = temp[idx]
                idx += 1
        
        return grid