# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:27:50 2020

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
葉ノード以外のノードを根ノードに向かって順に操作し、各ノードに対してheapifyメソッドを適用.
ただし、ヒープは各ノードが最大で２つの子ノードしかもたないため、n/2+1番目以降のノードはすべて葉ノードとなる。
@author: 81909
"""
def heapify(data, i):
    left = 2 * i + 1  # 左下の位置
    right = 2 * i + 2 # 右下の位置
    size = len(data) - 1
    min = i
    if left <= size and data[min] > data[left]:  # 左下のほうが小さい時
        min = left
    if right <= size and data[min] >  data[right]: # 右下のほうが小さい時
        min = right
    if min != i:  # 交換が発生するとき
        data[i], data[min] = data[min], data[i]
        heapify(data, min)  # ヒープを再構成
        
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
# ヒープを構成
for i in reversed(range(len(data))):
    # 葉ノード以外を処理
    heapify(data, i)

# ソートを実行    
sorted_data = []
for _ in range(len(data)):
    data[0], data[-1] = data[-1], data[0]  # 最後のノードと先頭を入れ替える
    sorted_data.append(data.pop())  # 最小のノードを取り出してソート済みにする
    heapify(data, 0)  # ヒープを再構成

print(sorted_data)
