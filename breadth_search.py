# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 10:18:36 2020

幅優先探索
@author: 81909
"""
tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [],[],[],[],[],[],[],[]]

data = [0]
while len(data) > 0:
    pos = data.pop(0)  # 先頭から取り出す。
    print(pos, end=' ')
    for i in tree[pos]:
        data.append(i)  # 末尾に追加
        