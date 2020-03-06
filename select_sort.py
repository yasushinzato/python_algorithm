# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:52:08 2020

選択ソート
     　　　　　　　　　　　　n(n-1)
(n-1)+(n-2)+・・・+1= ─────
　　　　　　　　　　　　　　　　　　２
の O(n^2) 計算量となる。
@author: 81909
"""
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(len(data)):
    min = i   # 最小値の位置をセット
    for j in range(i + 1, len(data)):
        if data[min] > data[j]:
            min = j  # 最小値がこうしんされたらその位置（添字）をセット
            
    # 最小値の位置と現在の要素を交換
    data[i], data[min] = data[min], data[i]
    
print(data)
