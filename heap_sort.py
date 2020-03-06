# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:54:20 2020

            A
           / \
          B   C
        / \  / \
       D  E  F  G

二分木をリストで構成するときは以下のイメージ
 0 1 2 3 4 5 6 
＿＿＿＿＿＿＿＿＿
|A|B|C|D|E|F|G|
￣￣￣￣￣￣￣￣￣
二分木は子のインデックスは親のインデックスを2倍＋１と２倍＋２したものと考えられる。
また、親のインデックスは、このインデックスから１をひいて２で割った商で求められる。
ヒープソート
O(n logn)
@author: 81909
"""
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# ヒープを構成
for i in range(len(data)):
    j = i
    while (j > 0) and (data[(j - 1) // 2] < data[j]):
        data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2] # 親と交換
        j = (j - 1) // 2 # 親の位置に移動
        
# ソートを実行
for i in range(len(data), 0, -1):
    # ヒープの先頭と交換
    data[i - 1], data[0] = data[0], data[i - 1]
    j = 0  # ヒープの先頭から開始
    while((2 * j + 1 < i - 1) and (data[j] < data[2 * j + 1]))\
      or ((2 * j + 2 < i - 1) and (data[j] < data[2 * j + 2])):     # 左下のほうが大きい(上段条件)   # 右下のほうが大きい（下段条件）
          if(2 * j + 2 == i - 1) or (data[2 * j + 1] > data[2 * j + 2]):
              # 左下と交換
              data[j], data[2 * j + 1] = data[2 * j + 1], data[j]
              # 左下に移動
              j = 2 * j + 1
          else:
              # 右下と交換
              data[j], data[2 * j + 2] = data[2 * j + 2], data[j]
              # 右下に移動
              j = 2 * j + 2

print(data)
