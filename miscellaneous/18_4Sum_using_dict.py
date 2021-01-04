'''

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []


Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

Time Complexity: O(n^3) , generally for k sum solution it's O(n^k-1)
Space Complexity: O(n) as we will have k recursion call to the ksum method and in the worst case k can be equal to n.
                  Additionally , at any moment of time dict can have at max of n elements.

'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def ksum(nums, target, k):

            res = []

            if not nums or (nums[0] * k > target or nums[-1] * k < target):
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):

                if i == 0 or nums[i] != nums[i - 1]:

                    for _, item in enumerate(ksum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + item)
            return res

        def twoSum(nums, target):

            res = []
            dt = {}
            j = 0
            for item, val in enumerate(nums):
                dt[val] = item

            while j < len(nums):

                if target - nums[j] in dt and dt[target - nums[j]] > j:
                    res.append([nums[j], target - nums[j]])

                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                j += 1

            return res

        nums.sort()
        return ksum(nums, target, 4)