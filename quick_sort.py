# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:00:17 2020

クイックソート
小さい単位に分割して処理することを再帰的に繰り返す。
分割する基準となる要素の選択が重要で、うまく選べば高速に処理できるが、選んだ値によっては全く分割されず、選択ソートと同じ時間がかかる。
基準となるデータをピボット(pivot)と呼び、この実装では「リストの最初の要素」とする。
        |6|15|4|2|8|5|11|9|7|13|
       / 6より小さな要素    6より大きな要素  \
      |4|2|5|    |6|  |15|8|11|9|7|13|
   /4を基準   ↓　　　　　　　 ↓　15より小         \
  |2| |4| |5|    |6|  |8|11|9|7|13|　　|15|
    ・・・（略）
|2|　|4| |5| |6| |7|  |8| |9| |11| |13| |15|
        
@author: 81909
"""
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

def quick_sort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0] # ピボットとしてリストの先頭を使用
    left, right, same = [], [], 0
    
    for i in data:
        if i < pivot:
            # ピボットより小さい場合はヒ左に
            left.append(i)
        elif i > pivot:
            # ピボットより大きい場合は右に
            right.append(i)
        else:
            same += 1
            
    left = quick_sort(left)  # 左側を再帰でソート
    right = quick_sort(right) # 右側を再帰でソート
    # ソートされたものとピボットの値をあわせて返す
    return left + [pivot] * same + right

print(quick_sort(data))
