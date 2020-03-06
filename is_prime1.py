# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:35:17 2020

@author: 81909
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    # ２からその数の平方根までループを繰り返す。
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: # 割り切れるか判定。割り切れれば素数ではない。
            return False
    return True  # １と自分自身だけだったので、素数。

for i in range(100000):
    if is_prime(i):
        print(i, end=' ')
        