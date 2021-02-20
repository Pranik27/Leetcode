# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:38:53 2021

@author: PRANIKP

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

Time Complexity:O(m*n)
Space Complexity:O(m*n)
"""

class Solution(object):
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def markIsland(row,col,grid):
        
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
                return 

            grid[row][col] = '0'

            markIsland(row - 1,col,grid)
            markIsland(row + 1,col,grid)
            markIsland(row,col - 1,grid)
            markIsland(row ,col + 1,grid)
        
        no_of_islands = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(0,rows):
            
            for col in range(0,cols):
                
                if grid[row][col] == '1':
                    no_of_islands += 1
                    markIsland(row,col,grid)
        
        return no_of_islands