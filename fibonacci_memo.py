# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:53:24 2020

線形オーダー　O(n)　でのフィボナッチ数列の実装。
@author: 81909
"""
memo = {1: 1, 2: 1}  # 辞書に終了条件の値をセット
# =============================================================================
# def fibonacci(n):
#     if n in memo:
#         return memo[n] # 辞書に登録されていれば、その値を返す
#     
#     memo[n] = fibonacci(n - 2) + fibonacci(n - 1)  # 辞書に登録がなければ登録する。
#     return memo[n]
# 
# =============================================================================
# 再帰処理のメモ化をライブラリ使って実装
import functools
@functools.lru_cache(maxsize = None)
def fibonacci(n):
    if n in memo:
        return memo[n]
    return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(20))
