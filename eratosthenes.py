# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:46:19 2020

@author: 81909
効率よく素数を求めるための「エラトステネスの篩」により素数を求める

PythonにはSymPyというライブラリがあり、
conda install sympy
もしくは
pip install sympy
でインストールする
"""

import math

def get_prime(n):
    if n <= 1:
        return []
    # 素数リスト２だけで作成。上限は変数の平方根まで
    prime = [2]
    limit = int(math.sqrt(n))
    
    # 基数のリストを作成
    data = [i + 1 for i in range(2, n, 2)]
    while limit > data[0]:
        # 素数リストに奇数の先頭を追加
        prime.append(data[0])
        # 奇数のリストのうち、割り切れない数だけを取り出す
        data = [j for j in data if j % data[0] != 0]
        
    return prime + data

print(get_prime(100000))