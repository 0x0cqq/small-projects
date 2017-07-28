#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-06-29 07:09:00
# @Author  : Chen Qiqian (qiqianchen@gmail.com)
# @Link    : https://github.com/ChenQiqian
# @Version : $Id$


import math
"""s1 = 72.0
s2 = 85.0
r = (s2 - s1) / s1 * 100
print("xiaomingde chengji tisheng le %.1f %%" % r)"""

"""L = ['Bart', 'Lisa', 'Adam']

for i in L:
    print("Hello,%s." % i)
"""


def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return "please give me a number"
    elif b**2 - 4 * a * c < 0:
        return "this quadratic don't have a answer"
    else:
        delta = math.sqrt(b**2 - 4 * a * c)
        x1 = (-b + delta) / (2 * a)
        x2 = (-b - delta) / (2 * a)
        return x1, x2


print(quadratic(1, 3, 2))  # => (-0.5, -1.0)
print(quadratic(1, 3, -4))  # => (1.0, -4.0)
