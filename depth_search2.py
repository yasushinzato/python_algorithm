# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 10:33:52 2020

深さ優先探索
帰りがけ順
@author: 81909
"""
tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [],[],[],[],[],[],[],[]]

def search(pos):
    for i in tree[pos]:
        search(i)
    print(pos, end=' ')  # 配下のノードを調べたあとに出力
search(0)
