# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 13:31:09 2020

ハノイの塔
@author: 81909
"""
# n => 残り枚数、　src => 移動元、 dist => 移動先、 via => 経由場所
def hanoi(n, src, dist, via):
    if n > 1:
        hanoi(n - 1, src, via, dist)  # n-1枚を移動元から経由場所に移す
        print(src + ' -> ' + dist)
        hanoi(n - 1, via, dist, src) # n-1枚を経由場所から移動先に移す
    else:
        print(src + ' -> ' + dist)

n = int(input())
hanoi(n, 'a', 'b', 'c')
