#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
