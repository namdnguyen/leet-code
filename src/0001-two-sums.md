# Problem 1 - Two Sums

https://leetcode.com/problems/two-sum/description/

## Instructions

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have ***exactly*** one solution, and you
may not use the same element twice.

### Example:

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

:type nums: List[int]
:type target: int
:rtype: List[int]
```


## Solution

```python
class Solution:
    def twoSum(self, nums, target):
        i = 0
        total = 0
        complements = []

        complements[:] = [target - i for i in nums]
        complements[:] = [i for i in nums if i in complements]

        if len(complements) > 2:
            while total != target:
                for i in range(len(complements)):
                    for j in range(i + 1, len(complements)):
                        total = complements[i] + complements[j]
                        if total == target:
                            break
                    if total == target:
                        break
            first = nums.index(complements[i])
            second = nums.index(complements[j])
        elif complements[0] == complements[1]:
            first = nums.index(complements[0])
            second = [i for i, e in enumerate(nums) if e == complements[0]]
            second = second[1]
        else:
            first = nums.index(complements[0])
            second = nums.index(complements[1])
        return [first, second]
```
