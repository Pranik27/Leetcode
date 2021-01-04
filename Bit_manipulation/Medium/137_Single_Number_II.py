'''

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.



Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99


Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.


Follow up: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Time Complexity: O(32 * n) for first approach and O(n) for second approach.
Space Complexity: O(1)

'''

#First

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for i in range(32):

            count = 0
            for x in nums:
                count += (x >> i) & 1

            rem = count % 3

            if i == 31 and rem:
                res -= (1 << 31)
            else:
                res |= rem * (1 << i)

        return res

#Second

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        fristseen = 0
        twiceseen = 0

        for x in nums:
            fristseen = (fristseen ^ x) & (~twiceseen)
            twiceseen = (twiceseen ^ x) & (~fristseen)

        return fristseen
