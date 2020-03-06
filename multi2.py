# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:44:02 2020
体積を求める場合の計算量
掛け算と出力にかかる時間をdとすると、内側のループを掛けて d×n 回、さらに外側のループも掛けると
全部で d×n×n×n=dn^3 の時間がかかる
O(n^3)
@author: 81909
"""
n = 10
for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            print(str(i) + '*' + str(j) + str(k) + '=' + str(i * j * k))
