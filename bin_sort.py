# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:47:46 2020

0～9の整数（10種類）だけで構成されるデータを並べ替える場合
@author: 81909
"""
data = [9, 4, 5, 2, 8,3, 7, 8, 3, 2, 6, 5, 7, 2, 9]

# 回数を保存するリスト 0~9　までの整数を並べ替えるので10で掛ける
result = [0] * 10

for i in data:
    # 回数をカウント
    result[i] += 1
    
for i in range(10):
    for j in range(result[i]):
        print(i, end=' ')

