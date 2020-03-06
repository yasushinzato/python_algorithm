# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:02:13 2020

線形オーダー　O(n)　でのフィボナッチ数列の実装。
辞書（連想配列）じゃなくてfor文での実装
@author: 81909
"""
def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])
    return fib[n - 1]

