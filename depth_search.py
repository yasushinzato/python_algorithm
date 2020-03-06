# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 10:25:51 2020

深さ優先探索
行きがけ順
@author: 81909
"""
tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [],[],[],[],[],[],[],[]]

def search(pos):
    print(pos, end=' ')  # 配下のノードを調べる前に出力
    for i in tree[pos]:
        search(i)
search(0)
