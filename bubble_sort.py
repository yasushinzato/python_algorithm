# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:09:39 2020

バブルソート
     　　　　　　　　　　　　n(n-1)
(n-1)+(n-2)+・・・+1= ─────
　　　　　　　　　　　　　　　　　　２
の O(n^2) 計算量となる。
データの並び順に関わらず、常に O(n^2) になる。
@author: 81909
"""
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# =============================================================================
# for i in range(len(data)):
#     for j in range(len(data) - i -1):  # ソート済みの部分以外でループ
#         if data[j] > data[j + 1]:
#             data[j], data[j + 1] = data[j + 1], data[j]
# # 上記の実装をリファクタリング。
# # 変更が発生しなかった場合、それ以降の処理は行わないようにして高速化する。
# 以下のロジックで、データがソートされていれば、 O(n) の計算量になる。
# =============================================================================
change = True
for i in range(len(data)):
    if not change:  # 交換が発生していなければ終了
        break
    change = False   # 交換が発生していないものとする。
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            change = True # 交換が発生
            
print(data)

