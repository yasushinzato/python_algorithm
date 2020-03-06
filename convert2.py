# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:20:21 2020

@author: 81909
"""

n = '10010'

result = 0
for i in range(len(n)):
    # 2^nで２進数の各桁ごとの数値を求めていき、最終結果を取得
    result += int(n[i]) * (2 ** (len(n) - i - 1))

print(result)
