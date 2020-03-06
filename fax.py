# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:10:01 2020

同じ文字が連続する場合、その文字の出現回数を数えて圧縮するアルゴリズム
この例では0と1の２つの文字だけで構成される文字列を回数だけで表現。FAXの圧縮などで使われている方法
@author: 81909
"""
data = '00000001111111110011100000000111'

flag = 0# boolean型だと切り替わったときの比較用の変数が必要になるため。
count = 0
result = []
for i in list(data):
    # データは1か0だけなので、切り替えが発生していない場合はカウントを継続
    if int(i) == flag:
        count += 1
    else:
        result.append(count)
        count = 1
        flag = 1 - flag

result.append(count)
print(result)
