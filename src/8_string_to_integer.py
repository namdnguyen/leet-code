import re


class Solution:
    def myAtoi(self, str):
        """
        Implement atoi which converts a string to an integer.

        The function first discards as many whitespace characters as necessary
        until the first non-whitespace character is found. Then, starting from
        this character, takes an optional initial plus or minus sign followed
        by as many numerical digits as possible, and interprets them as a
        numerical value.

        The string can contain additional characters after those that form the
        integral number, which are ignored and have no effect on the behavior
        of this function.

        If the first sequence of non-whitespace characters in str is not a
        valid integral number, or if no such sequence exists because either str
        is empty or it contains only whitespace characters, no conversion is
        performed.

        If no valid conversion could be performed, a zero value is returned.

        Note:

        Only the space character ' ' is considered as whitespace character.
        Assume we are dealing with an environment which could only store
        integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. If
        the numerical value is out of the range of representable values,
        INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

        Example 1:

        Input: "42"
        Output: 42

        Example 2:

        Input: "   -42"
        Output: -42
        Explanation: The first non-whitespace character is '-', which is the
                     minus sign. Then take as many numerical digits as
                     possible, which gets 42.

        Example 3:

        Input: "4193 with words"
        Output: 4193
        Explanation: Conversion stops at digit '3' as the next character is not
                     a numerical digit.

        Example 4:

        Input: "words and 987"
        Output: 0
        Explanation: The first non-whitespace character is 'w', which is not a
                     numerical digit or a +/- sign. Therefore no valid
                     conversion could be performed.

        Example 5:

        Input: "-91283472332"
        Output: -2147483648
        Explanation: The number "-91283472332" is out of the range of a 32-bit
                     signed integer. Thefore INT_MIN (−2^31) is returned.

        :type str: str
        :rtype: int

        URL: https://leetcode.com/problems/string-to-integer-atoi/description/
        """
        string = str.replace(' ', '')
        num_reg = re.compile('\\d+')
        match = num_reg.search(string)

        if string == "":
            converted = 0
        elif match is None:
            converted = 0
        elif (string[0] != '-' and
              string[0] != '+' and
              string[0].isdigit() is False):
            converted = 0
        elif string[0] == '-' and string[1].isdigit() is False:
            converted = 0
        elif string[0] == '+' and string[1].isdigit() is False:
            converted = 0
        else:
            start = match.start()
            is_negative = bool(string[start - 1] == '-')

            if is_negative is True:
                num_int = int(match.group()) * -1
            else:
                num_int = int(match.group())

            if num_int > 2**31 - 1:
                converted = 2**31 - 1
            elif num_int < -2**31:
                converted = -2**31
            else:
                converted = num_int

        return converted
