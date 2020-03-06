# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:55:26 2020

キューは先入れ先出し（FIFO）
新しいデータほど長く残る。
キューのイメージとしては、ロケットペンシルのように入れたら古いほうが押し出される。
もしくはベルトコンベアーで先に入れたものが先に取り出されるイメージ。

queue.pyというファイル名にするとqueueモジュールが読み込めずにエラーが発生する。
Python3.7 からSimpleQueueというクラスも用意されている。
@author: 81909
"""
import queue

q = queue.Queue()
# q = queue.SimpleQueue()  # 3.7から実装されたクラス


q.put(3)
q.put(5)
q.put(2)

temp = q.get()  # キューからデータ取り出し
print(temp)

temp = q.get()  # キューからデータ取り出し
print(temp)

q.put(4)  # キューにデータを追加し、先入れ先出しであることを確認する。


temp = q.get()  # キューからデータ取り出し
print(temp)
