# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 14:52:50 2020

エレベータを使って１階からN階まで移動するとき、停止する階の組み合わせが何通りあるかを調べるのに
2^n-2
@author: 81909
"""

def search(N):
    combination = 2**(N-2)
    return combination

print(str(search(10)) + '通り' )
    