'''

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.



Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99


Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
[Soln] : can we achieved using deQueue.
What if the matrix is so large that you can only load up a partial row into the memory at once?
[Soln]: Can be achieved by spitting the matix col wise , but need to make sure at least one column should be same in the subsequent split.

Time Complexity: O(m * n)
Space Complexity: O(1)
'''


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        row_len = len(matrix) - 1
        col_len = len(matrix[0])

        for x in range(row_len, 0, -1):

            for y in range(1, col_len):

                if matrix[x][y] != matrix[x - 1][y - 1]:
                    return False

        return True