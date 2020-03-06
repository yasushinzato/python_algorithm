# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:49:11 2020

スタックは後入れ先出し（LIFO）
古いデータほど長く残る。
スタックのイメージとしては、段ボール箱を積み重ねたとき、一番上から順序よく取っていくやりかた。
@author: 81909
"""
stack = []

stack.append(3)
stack.append(5)
stack.append(2)

temp = stack.pop()  # スタックからデータ取り出し
print(temp)

temp = stack.pop()  # スタックからデータ取り出し
print(temp)

stack.append(4)  # スタックにデータ追加し、後入れ先出しを確認

temp = stack.pop()  # スタックからデータ取り出し
print(temp)

