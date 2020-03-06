# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:38:27 2020

@author: 81909
"""
import heapq

def heap_sort(array):
    h = array.copy()
    heapq.heapify(h) # ヒープを構成
    return [heapq.heappop(h) for _ in range(len(array))]  # 取り出しながらソート済みのリストを作成

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
print(heap_sort(data))

