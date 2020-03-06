# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 16:11:43 2020

挿入ソート
     　　　　　　　 　n(n-1)
1+2+・・・+(n-1)= ─────
　　　　　　　　　　　　 　　２
の O(n^2) 計算量となる。
しかし、一度も交換が発生しない場合は比較のみのため、O(n) となる。
@author: 81909
"""
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(1, len(data)):
    temp = data[i]  # 現在の要素を一時的に記録
    j = i - 1       # 直前の位置を記録
    while (j >= 0) and (data[j] > temp):
        data[j + 1] = data[j]  # 要素を1つずつ後ろにずらす
        j -= 1
    data[j + 1] = temp  # 一時的な領域から戻す

print(data)