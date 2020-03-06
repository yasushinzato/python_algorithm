# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:33:51 2020

マージソート
        |6|15|4|2|8|5|11|9|7|13|
       /         /  \           \
      |6|15|4|2|8|  |5|11|9|7|13|
    ・・・（略）
  |6|　|15| |4| |2| |8|  |5| |11| |9| |7| |13|
    ・・・（略）   結合していくときにソートする。
    |6|15|   |2|4|8|    |5|11|    |7|9|13|

        |2|4|5|6|7|8|9|11|13|15|
     
2つのリストを統合する処理は、リスト先頭の値を比較して取り出すことを繰り返すだけなので、O(n)
次に、統合する段数を考え、n個のリストを1つになるまで結合した場合の段数はlog2nとなり、
全体の計算時間は O(n logn) となる。
マージソートの特徴として、メモリに入り切らない大容量のデータにも使える。
複数のディスク装置にあるデータをそれぞれでソートしておき、それを結合しながらソート済みのデータを作成するといったことが可能。    

@author: 81909
"""
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2   # 半分の位置を計算
    # 再帰的に分割
    left = merge_sort(data[:mid]) # 左側を分割
    right = merge_sort(data[mid:]) # 右側を分割
    # 結合
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while(i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i]) # 左側から1つ取り出して追加
            i += 1
        else:
            result.append(right[j]) # 右側から１つ取り出して追加
            j += 1
            
    # 残りを纏めて追加
    if i < len(left):
        result.extend(left[i:])  # 左側の残りを追加
    if j < len(right):
        result.extend(right[j:])  # 右側の残りを追加
    return result

print(merge_sort(data))

