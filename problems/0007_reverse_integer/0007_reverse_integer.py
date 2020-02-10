#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def reverse(self, x: int) -> int:
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
