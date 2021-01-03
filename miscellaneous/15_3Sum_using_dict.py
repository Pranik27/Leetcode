'''

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Time Complexity: O(n^2)
Space Complexity: O(n^2) . Dict takes O(n) SC and in the worst case we will store in the output list O(n-2) * O(n-1) records.
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        dt = {}
        res = []

        for idx, item in enumerate(nums):
            dt[item] = idx

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            while j < len(nums):

                target = -(nums[i] + nums[j])

                if target in dt and dt[target] > j:
                    res.append([nums[i], nums[j], target])

                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1

                j += 1

        return res