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
Space Complexity: O(n^2) ,in the worst case we will store in the output list O(n-2) * O(n-1) records.
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []

        nums.sort()

        triplets = []

        for idx in range(len(nums) - 2):

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:

                if nums[left] + nums[right] + nums[idx] == 0:
                    triplets.append([nums[idx], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + nums[idx] > 0:
                    right -= 1
                else:
                    left += 1

        return triplets