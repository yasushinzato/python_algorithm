# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:32:07 2020
掛け算の場合の計算量
掛け算とprint文を1回実行するのにかかる時間をcとすると、内側のループを掛けて c×n 回、さらに外側のループも掛けると
全部でc×n×n=ｃn^2 の時間がかかる
O(n^2)
@author: 81909
"""
n = 10
for i in range(1, n):
    for j in range(1, n):
        print(str(i) + '*' + str(j) + ' = ' + str(i * j))
        