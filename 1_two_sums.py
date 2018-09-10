class Solution:
    def twoSum(self, nums, target, verbose = False):
        """
        url: https://leetcode.com/problems/two-sum/description/
        Given an array of integers, return indices of the two numbers such that
        they add up to a specific target.

        You may assume that each input would have exactly one solution, and you
        may not use the same element twice.

        Example:

        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        sum = None
        while sum != target:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    sum = nums[i] + nums[j]
                    if verbose == True:
                        print(sum)
                    if sum == target:
                        break
                if sum == target:
                    break
            return [i, j]
