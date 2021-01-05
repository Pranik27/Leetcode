'''

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20

Time Complexity: O(n)
Space Complexity: O(1) , if we ignore the output matrix space.
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        top, bottom, left, right = 0, n - 1, 0, n - 1
        res = [[0] * n for rows in range(n)]
        num = 1
        mode = 0

        while top <= bottom and left <= right:

            if mode == 0:

                for i in range(left, right + 1):
                    res[top][i] = num
                    num += 1

                top += 1
            elif mode == 1:

                for i in range(top, bottom + 1):
                    res[i][right] = num
                    num += 1

                right -= 1
            elif mode == 2:

                for i in range(right, left - 1, -1):
                    res[bottom][i] = num
                    num += 1

                bottom -= 1
            else:

                for i in range(bottom, top - 1, -1):
                    res[i][left] = num
                    num += 1

                left += 1

            mode = (mode + 1) % 4
            print(res)

        return res
