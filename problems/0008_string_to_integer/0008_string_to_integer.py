#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class Solution:
    def myAtoi(self, str: str) -> int:
        string = str.strip()
        num_reg = re.compile("\\d+")
        match = num_reg.search(string)

        if string == "":
            converted = 0
        elif match is None:
            converted = 0
        elif string[0] != "-" and string[0] != "+" and string[0].isdigit() is False:
            converted = 0
        elif string[0] == "-" and string[1].isdigit() is False:
            converted = 0
        elif string[0] == "+" and string[1].isdigit() is False:
            converted = 0
        else:
            start = match.start()
            if match.start() != 0:
                is_negative = bool(string[start - 1] == "-")
            else:
                is_negative = False

            if is_negative is True:
                num_int = int(match.group()) * -1
            else:
                num_int = int(match.group())

            if num_int > 2 ** 31 - 1:
                converted = 2 ** 31 - 1
            elif num_int < -(2 ** 31):
                converted = -(2 ** 31)
            else:
                converted = num_int

        return converted
