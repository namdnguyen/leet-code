# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
#
# Example 2:
#
# Input: -123
# Output: -321
#
# Example 3:
#
# Input: 120
# Output: 21
#
# Note:
# Assume we are dealing with an environment which could only store
# integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For
# the purpose of this problem, assume that your function returns 0 when
# the reversed integer overflows.
#
# :type x: int
# :rtype: int
#
# URL: https://leetcode.com/problems/reverse-integer/description/


class Solution:
    def reverse(self, x):
        is_negative = bool(x < 0)
        string = str(abs(x))
        string_list = list(reversed(string))
        reversed_string = "".join(string_list)

        if is_negative is True:
            reversed_int = int(reversed_string) * -1
        else:
            reversed_int = int(reversed_string)

        # Check if reversed integer overflows
        if reversed_int > 2**31 or reversed_int < -2**31:
            reversed_int = 0

        return reversed_int
