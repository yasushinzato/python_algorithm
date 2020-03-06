# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:38:58 2020

指数オーダー O(a^n) での実装。
同じ数を何回も処理するため、数が多くなると処理時間も多くなる。
@author: 81909
"""

def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(32))
