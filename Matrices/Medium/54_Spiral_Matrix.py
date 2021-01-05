'''

Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

Time Complexity: O(n)
Space Complexity: O(1), if output list space is neglected.
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        mode = 0
        res = []

        while top <= bottom and left <= right:

            if mode == 0:

                for i in range(top, right + 1):
                    res.append(matrix[top][i])

                top += 1
            elif mode == 1:

                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])

                right -= 1
            elif mode == 2:

                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])

                bottom -= 1
            else:

                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])

                left += 1

            mode = (mode + 1) % 4

        return res

